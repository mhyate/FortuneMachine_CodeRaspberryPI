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
#pragma config	OSCIOFCN = OFF // OSCO Pin Configuration (OFF : CLKo (Fcy) sur RA3)
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
//#define     TEST_ICSP_OSC
//#define     TEST_MISC_GPIO
//#define     TEST_IHM_TX
#define     TEST_PRINTER




/* Déclarations des variables globales 	*/
unsigned char   NbGps = 0;

//------------------------------------------------------------------------------
/* TEST ICSP + Config oscillateur                                             */
/* Visualiser RA3 (broche 10) : signal rectangulaire fréq proche de 4MHz      */
//------------------------------------------------------------------------------

#ifdef TEST_ICSP_OSC

int main(void)
{
// Set oscillator freq to 8MHz
CLKDIVbits.RCDIV = 0b000;
while(1)
    {
    
    }
}					
#endif
//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
/* TEST Misc GPIO                                                             */
/* Visualiser Les 4 signaux MISC : signaux quasi carrés périodes proches 1 ms */
//------------------------------------------------------------------------------
#ifdef TEST_MISC_GPIO

#define     MISC0        LATAbits.LATA0
#define     TRIS_MISC0   TRISAbits.TRISA0

#define     MISC1        LATAbits.LATA1
#define     TRIS_MISC1   TRISAbits.TRISA1

#define     MISC2        LATBbits.LATB10
#define     TRIS_MISC2   TRISBbits.TRISB10

#define     MISC3        LATBbits.LATB11
#define     TRIS_MISC3   TRISBbits.TRISB11

int main(void)
{
unsigned int i;
// Set oscillator freq to 8MHz
CLKDIVbits.RCDIV = 0b000;

// Config Misc GPIOs
TRIS_MISC0 = 0;
TRIS_MISC1 = 0;
TRIS_MISC2 = 0;
TRIS_MISC3 = 0;

while(1)
    {
    MISC0 = ~MISC0;
    MISC1 = ~MISC1;
    MISC2 = ~MISC2;
    MISC3 = ~MISC3;
    for (i = 0; i < 310 ; i++); 
    }
}					
#endif
//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
/* TEST IHM_TX                                           */
/* Emission cyclique alphabet MAJUSCULE sur IMH_TxD (RP15)                    */
/* Config UART : 57600 8N1                                                    */
//------------------------------------------------------------------------------

#ifdef TEST_IHM_TX

int main(void)
{
unsigned char Byte; 
unsigned int i;
    
// Set oscillator freq to 8MHz
CLKDIVbits.RCDIV = 0b000;

// UART3 : HMI (COM)
ANSBbits.ANSELB14 = 0;       // Ne pas oublier d'activer le buffer in#
RPOR7bits.RP15R = 19;        // Remap U3TX to RP15
RPINR17bits.U3RXR  = 14;     // Remap U3RX to RP14

// UART 56kbps, most standard mode
COM_UXBRG = 16;        // 56 kbps avec BRGH=1, valeur 17 en théorie 
//COM_UXBRG = 104;        // 9600 bps pour tests
COM_UXMODE = 0x8008;
COM_UXSTA = 0x0400;

Byte = 'A';
while(1)
    {
    while(COM_BFBIT); // wait while Tx buffer full
    COM_UXTXREG = Byte;
    
    if (Byte < 'Z') Byte++;
    else Byte = 'A';
    
    for (i = 0; i < 65000 ; i++); 
    }
}					
#endif
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
/* TEST printer                                                               */
/* Prints a test page, line feed x2 and "Hello World !"                      */
//------------------------------------------------------------------------------

#ifdef TEST_PRINTER

int main(void)
{
// Set oscillator freq to 8MHz
CLKDIVbits.RCDIV = 0b000;

// UART2 : UART PRINTER - Tx Pin only
    RPOR3bits.RP7R = 5;         // Remap U2TX to RP7
    
// UART 19200 bps, most standard mode
    PRN_UXBRG = 51;        // 19200 bps avec BRGH=1, valeur 51 en théorie
    PRN_UXMODE = 0x8008;
    PRN_UXSTA = 0x0400;
    
     __delay_ms(500);
     __delay_ms(500);
     __delay_ms(500);
     
     //printer_print_test_page();
     
     __delay_ms(500);
     __delay_ms(500);
          
     printer_putch(PRN_LF);
          
      __delay_ms(500);
     __delay_ms(500);
     
     printer_print("Hello World !");
     
while(1)
    {
    
    }
}					
#endif
//------------------------------------------------------------------------------



//------------------------------------------------------------------------------





//------------------------------------------------------------------------------





