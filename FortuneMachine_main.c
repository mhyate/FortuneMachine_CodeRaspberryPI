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

#include "lib_Fortune.h"   // Inclusion du fichier .h "Applicatif" renommé

/*----------------------------------------------------------------------------*/
/*Insérer Ici les bits de configuration pour le µC 							  */
/* -> Copier / Coller depuis le fichier Config_Pic24.txt					  */
/*----------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------*/
/* PIC24FJ64GB202                                                           */
/*--------------------------------------------------------------------------*/
#pragma config	DSWDTPS =  DSWDTPS0 // Deep Sleep Watchdog Timer Postscale Select bits (0 à 1F)
#pragma config	DSWDTOSC =  SOSC // DSWDT Reference Clock Select (SOSC / LPRC)
#pragma config	DSBOREN = OFF // Deep Sleep BOR Enable bit (ON / OFF)
#pragma config	DSWDTEN = OFF // Deep Sleep Watchdog Timer Enable (ON / OFF)
#pragma config	DSSWEN = OFF // DSEN Bit Enable (ON / OFF)

#pragma config	PLLDIV = DISABLED // USB 96 MHz PLL Prescaler Select bits
#pragma config	I2C1SEL =  DISABLE // Alternate I2C1 enable bit (ENABLE / DISABLE)
#pragma config	IOL1WAY = OFF // PPS IOLOCK Set Only Once Enable bit

#pragma config	WPFP = WPFP0 // Write Protection Flash Page Segment Boundary
#pragma config	SOSCSEL = OFF	 // SOSC Selection bits
#pragma config	WDTWIN = PS75_0 // Window Mode Watchdog Timer Window Width Select
#pragma config	PLLSS = PLL_FRC // PLL Secondary Selection Configuration bit

#pragma config	BOREN = OFF // Brown-out Reset Enable
#pragma config	WPDIS = WPDIS // Segment Write Protection Disable
#pragma config	WPCFG = WPCFGDIS // Write Protect Configuration Page Select

#pragma config	POSCMD = NONE // Primary Oscillator Select (EC / XT / HS / NONE)
#pragma config	WDTCLK = LPRC // WDT Clock Source Select bits
#pragma config	OSCIOFCN = ON // OSCO Pin Configuration (OFF : CLKo (Fcy) sur RA3)
#pragma config	FCKSM = CSDCMD // Clock Switching and Fail-Safe Clock Monitor Configuration bits
#pragma config	FNOSC = FRC // Initial Oscillator Select
#pragma config	ALTRB6 = RETAIN	// Alternate RB6 pin function enable bit
#pragma config	ALTCMPI = CxINC_RX	// Alternate Comparator Input bit
#pragma config	WDTCMX = WDTCLK // WDT Clock Source Select bits
#pragma config	IESO = OFF	// Internal External Switchover
#pragma config	WDTPS = PS128 // Watchdog Timer Postscaler Select
#pragma config	FWPSA = PR32 // WDT Prescaler Ratio Select
#pragma config	WINDIS = OFF // Windowed WDT Disable
#pragma config	FWDTEN = OFF // Watchdog Timer Enable
#pragma config	ICS = PGx1 // Emulator Pin Placement Select bits
#pragma config	LPCFG = OFF // Low power regulator control
#pragma config	GWRP = OFF //	General Segment Write Protect
#pragma config	GCP = OFF //	General Segment Code Protect
#pragma config	JTAGEN = OFF //	JTAG Port Enable

/* Directives de compilation		*/


/* Déclarations des variables globales 	*/
uint8_t   NbGps = 0;

/* Programme Principal			*/
int main(void)
{
// Variables locales au main
tRMC_MINIMAL_DATA Data; 
tRxTypeFrame    TypeTrame;
tCoinValue      Coin;
        
Initialiser();		// Appel fonction d'initialisation

MISC0 = 0;
while(1)
    {
    // Check for incomming Coins
    
    if (coinacc_check(&Coin) != NO_COIN)
    {
        if (Coin == NO_COIN)com_send_error(ID_ERROR_COIN_ACCEPTOR,(uint8_t *)"Erreur Coin Acceptor"); 
        else com_send_coin_ok(Coin);
        coinacc_clear();
    }
        
    // Check for incoming HMI frame
    if (com_check())
    {
        
        TypeTrame = com_get_frame_type();
        
        switch(TypeTrame)
        {
            case FR_PRINT :         com_puts((uint8_t *)"Trame PRINT\n");break;
            case FR_GET_GPS_DATE :  com_send_gps_date(&Data);break;
            case FR_GET_GPS_POS :   com_send_gps_pos(&Data);break;
            
            case FR_ERROR :         com_send_error(ID_FRAME_ERROR,(uint8_t *)"Trame erreur");break;
            default:                com_send_error(ID_UNKNOWN_FRAME,(uint8_t *)"Trame inconnue");break;
        }
                 
        com_clear();
    }
    
    // Check for incoming GPS frame
    if (gps_check())
        {
            if (gps_decode(&Data) == TRUE)
            {
                NbGps++;
                if (NbGps >= FORCE_SEND_GPS)            
                {
                    com_send_gps_pos(&Data);
                    NbGps = 0;
                }
                else
                {
                //com_send_info((uint8_t *)"---info---"); // Debug purpose only
                }
            }
            gps_clear();
        }
    
    }
}					

