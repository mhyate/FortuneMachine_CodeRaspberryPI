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


#include "lib_com.h" // Inclusion du fichier .h "Applicatif" renommé

/* Directives de compilation		*/

/* Déclarations des variables globales 	*/
uint8_t         comRxBuffer[1024]="";
uint8_t         comRxCar = 0;
uint8_t         comRxPtr = 0;
tRxStatus       comEtatRx = WAIT_START;

uint8_t         comTxBuffer[1024]="";

/*	Implémentation du code */
//----------------------------------------------------------------------------
void _ISR __attribute__((no_auto_psv)) COM_RXISR(void)
{
    comRxCar = COM_UXRXREG;
    switch(comEtatRx)
    {
        case WAIT_START : 
            if (comRxCar == COM_START)
            {
               comRxPtr = 0;
               comEtatRx = RX_ON;
            }
            break;
        case RX_ON:
            if (comRxCar != COM_CR)
            {
                comRxBuffer[comRxPtr] = comRxCar;
                comRxPtr++;
            }
            else
            {
                comEtatRx = WAIT_RD_BUFFER;
            }
            break;
        case WAIT_RD_BUFFER:
            break;
        default: break;
            
    }
    
    COM_RXIF = 0;
} // _InterruptVector
//----------------------------------------------------------------------------

//------------------------------------------------------------------------------
void com_init(void)
{
    // UART 56kbps, most standard mode
    COM_UXBRG = 16;           // 56 kbps avec BRGH=1, valeur 17 en théorie
    //COM_UXBRG = 104;        // 9600 bps pour tests
    COM_UXMODE = 0x8008;
    COM_UXSTA = 0x0400;
    
    // Autorisation IRQ RX
    COM_RXIF = 0;
    COM_RXIE = 1;
}
//------------------------------------------------------------------------------
void    com_putch(uint8_t Byte)
{
    while(COM_BFBIT); // wait while Tx buffer full
    COM_UXTXREG = Byte;
}
//------------------------------------------------------------------------------
void    com_puts(uint8_t *pStr)
{
    while (*pStr != '\0')
    {
        while (COM_BFBIT); // wait while Tx buffer full
        COM_UXTXREG = *pStr;
        pStr++;
    }
}
//------------------------------------------------------------------------------
//----------------------------------------------------------------------------
uint8_t com_check(void)
{
        if (comEtatRx == WAIT_RD_BUFFER) return TRUE; // true if frame waiting
        else return FALSE;    
}
//----------------------------------------------------------------------------
void    com_clear(void)
{
    comEtatRx = WAIT_START; 
}
//----------------------------------------------------------------------------
void    com_send_gps_pos(tRMC_MINIMAL_DATA *pData)
{
    sprintf((char*)comTxBuffer,"<GPS:%d,%d,%d,%c,%d,%d,%d,%c,%c\n",   
                                                pData->latDeg,
                                                pData->latMin,
                                                pData->latDec,
                                                pData->latNS,
                                                pData->longDeg,
                                                pData->longMin,
                                                pData->longDec,
                                                pData->longEW,
                                                pData->ValidData);

    com_puts(comTxBuffer);
}
//----------------------------------------------------------------------------
void    com_send_coin_ok(uint8_t aCoinValue)
{
    sprintf((char*)comTxBuffer,"<COI:%d\n",aCoinValue);
    com_puts(comTxBuffer);
}
//----------------------------------------------------------------------------
void    com_send_gps_date(tRMC_MINIMAL_DATA *pData)
{
    sprintf((char*)comTxBuffer,"<GDT:%d,%d,%d,%d,%d,%d,%c\n",
                                                    pData->year,
                                                    pData->month,
                                                    pData->day,
                                                    pData->hh,
                                                    pData->mm,
                                                    pData->ss,
                                                    pData->ValidData);

    com_puts(comTxBuffer);
}
//----------------------------------------------------------------------------
tRxTypeFrame com_get_frame_type(void)
{
       
    if (strncmp((const char*)comRxBuffer,"PRN:",4) == 0) return FR_PRINT;
    if (strncmp((const char*)comRxBuffer,"GDT?",4) == 0) return FR_GET_GPS_DATE;
    if (strncmp((const char*)comRxBuffer,"GPS?",4) == 0) return FR_GET_GPS_POS;
    
    return FR_ERROR;
}
//----------------------------------------------------------------------------
void    com_send_info(uint8_t *apInfo)
{
    sprintf((char*)comTxBuffer,"<NFO:%s\n",apInfo);
    com_puts(comTxBuffer);
}
//----------------------------------------------------------------------------
void    com_send_error(uint8_t aCode, uint8_t *apMsg)
{
    sprintf((char*)comTxBuffer,"<ERR:%d,%s\n",aCode,apMsg);
    com_puts(comTxBuffer);
}
//----------------------------------------------------------------------------
//----------------------------------------------------------------------------
//----------------------------------------------------------------------------
//----------------------------------------------------------------------------
//----------------------------------------------------------------------------
//----------------------------------------------------------------------------
//----------------------------------------------------------------------------
