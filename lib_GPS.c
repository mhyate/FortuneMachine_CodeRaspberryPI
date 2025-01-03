/***************************************************************************
* Nom du prg 	:  
* Description	: 
*
* Auteur	: 
* Créé le	:
* Compilateur	: 
***************************************************************************
* Modifié le  	:
***************************************************************************/


#include "lib_GPS.h" // Inclusion du fichier .h "Applicatif" renommé
//----------------------------------------------------------------------------
/* Directives de compilation		*/

//----------------------------------------------------------------------------
/* Déclarations des variables globales 	*/
uint8_t   gpsRxBuffer[100]="";
uint8_t   gpsRxCar = 0;
uint8_t   gpsRxPtr = 0;
tRxStatus       gpsEtatRx = WAIT_START;

uint8_t   Trame[NB_CHAMPS][TAILLE_CHAMP];

tGpsReceiveStatus   GpsReceiveStatus = GPS_RECEIVE_ON;

//----------------------------------------------------------------------------
/*	Implémentation du code */
//----------------------------------------------------------------------------
void _ISR __attribute__((no_auto_psv)) GPS_RXISR(void)
{
    gpsRxCar = GPS_UXRXREG;
    switch(gpsEtatRx)
    {
        case WAIT_START : 
            if (gpsRxCar == NMEA_START)
            {
               gpsRxPtr = 0;
               gpsEtatRx = RX_ON;
            }
            break;
        case RX_ON:
            if (gpsRxCar != NMEA_CR)
            {
                gpsRxBuffer[gpsRxPtr] = gpsRxCar;
                gpsRxPtr++;
            }
            else
            {
                gpsEtatRx = WAIT_RD_BUFFER;
            }
            break;
        case WAIT_RD_BUFFER:
            break;
        default: break;
            
    }
    GPS_RXIF = 0;
} // _InterruptVector
//----------------------------------------------------------------------------
void    gps_init(void)
{
    // UART 9600 bps, most standard mode
    GPS_UXBRG = 104;        // 9600 bps avec BRGH=1, valeur 103 en théorie
    GPS_UXMODE = 0x8008;
    GPS_UXSTA = 0x0400;
    
    // Autorisation IRQ RX
    GPS_RXIE = 1;
}
//----------------------------------------------------------------------------
/*
void    gps_putch(uint8_t Byte)
{
    while (GPS_BFBIT); // wait while Tx buffer full
    GPS_UXTXREG = Byte;
}
*/
//----------------------------------------------------------------------------
uint8_t    gps_check(void)
{
        if (gpsEtatRx == WAIT_RD_BUFFER) return 0x01; // true if frame waiting
        else return 0;    
}
//----------------------------------------------------------------------------
void            gps_clear(void)
{
    gpsEtatRx = WAIT_START;    
}
//----------------------------------------------------------------------------
uint8_t gps_decode(tRMC_MINIMAL_DATA *pData)
{   
    uint8_t Res;
    if (gpsEtatRx != WAIT_RD_BUFFER) return 0;
    
    if (strncmp((char*)gpsRxBuffer,"GPRMC,",6) == 0)
    {
        SplitTrame(gpsRxBuffer);
        // Décodage Heure : champ 1 [HHMMSS.xxx]
        pData->hh = get2digits(Trame[1]);
        pData->mm = get2digits(Trame[1]+2);
        pData->ss = get2digits(Trame[1]+4);
        // Décodage date : champ 9 [DDMMYY]
        pData->day = get2digits(Trame[9]);
        pData->month = get2digits(Trame[9]+2);
        pData->year = get2digits(Trame[9]+4);
        // Décodage latitude : champ 3 [ddmm.____] + champ 4 : N/S
        pData->latDeg = get2digits(Trame[3]);
        pData->latMin = get2digits(Trame[3]+2);
        pData->latDec = get4digits(Trame[3]+5);
        pData->latNS = Trame[4][0];
        // Décodage longiture : champ 5 [dddmm.____] + champ 6 : O/E
        pData->longDeg = get3digits(Trame[5]);
        pData->longMin = get2digits(Trame[5]+3);
        pData->longDec = get4digits(Trame[5]+6);
        pData->longEW = Trame[6][0];
        
        pData->ValidData = Trame[2][0];
        
        Res = 0x01;
    }
    else
    {
        Res = 0x00;
    }        
    
    return Res;
}
//----------------------------------------------------------------------------
void    gps_receive_on(void)
{
    gpsRxPtr = 0;   // Raz rx pointer
    gpsEtatRx = WAIT_START;
    GPS_RXIE = 1;   // Autorisation IRQ Rx UART GPS
}
//----------------------------------------------------------------------------
void    gps_receive_off(void)
{
    GPS_RXIE = 0;   // Interdiction IRQ Rx UART GPS
}
//----------------------------------------------------------------------------
tGpsReceiveStatus gps_get_receive_status(void)
{
    return GpsReceiveStatus;
}
//----------------------------------------------------------------------------
signed char SplitTrame(uint8_t * pBuffer)
{
    signed char NbChamps = 0;
    char *Pointer;
    
    Pointer = strtok((char*)pBuffer, ",");
    while (Pointer != NULL)
        {
        strcpy((char*)Trame[NbChamps],Pointer);
        NbChamps++;
        Pointer = strtok(NULL, ","); 
        }
    return NbChamps;
}
//----------------------------------------------------------------------------
signed char   get2digits(uint8_t* pBuffer)
{
    signed char Res; 
    
    if ((pBuffer[0] < '0') || (pBuffer[0] > '9')) return -1;
    if ((pBuffer[1] < '0') || (pBuffer[1] > '9')) return -1;
    
    Res = ((pBuffer[0]-0x30)* 10) + (pBuffer[1]-0x30);
    return Res;
}
//----------------------------------------------------------------------------
signed int    get4digits(uint8_t* pBuffer)
{
   signed int Res; 
    
    if ((pBuffer[0] < '0') || (pBuffer[0] > '9')) return -1;
    if ((pBuffer[1] < '0') || (pBuffer[1] > '9')) return -1;
    if ((pBuffer[2] < '0') || (pBuffer[2] > '9')) return -1;
    if ((pBuffer[3] < '0') || (pBuffer[3] > '9')) return -1;
   
    Res = ((pBuffer[0]-0x30) * 1000) + ((pBuffer[1]-0x30) * 100) + ((pBuffer[2]-0x30) * 10) + (pBuffer[3]-0x30);
    return Res; 
}
//----------------------------------------------------------------------------
signed int    get3digits(uint8_t* pBuffer)
{
   signed int Res; 
    
    if ((pBuffer[0] < '0') || (pBuffer[0] > '9')) return -1;
    if ((pBuffer[1] < '0') || (pBuffer[1] > '9')) return -1;
    if ((pBuffer[2] < '0') || (pBuffer[2] > '9')) return -1;
      
    Res = ((pBuffer[0]-0x30) * 100) + ((pBuffer[1]-0x30) * 10) + (pBuffer[2]-0x30);
    return Res; 
}
//----------------------------------------------------------------------------

//----------------------------------------------------------------------------



