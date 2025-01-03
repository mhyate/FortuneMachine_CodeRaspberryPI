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

#include "lib_Fortune.h" // Inclusion du fichier .h "Applicatif" renommé

/* Directives de compilation		*/

/* Déclarations des variables globales 	*/

/*	Implémentation du code */
void Initialiser(void)
{
    // Set oscillator freq to 8MHz
    CLKDIVbits.RCDIV = 0b000;
    
    // GPIO
    TRIS_MISC0 = 0;
    MISC0 = 0;
    
    // UART1 : UART GPS - Rx Pin only 
    ANSBbits.ANSELB13 = 0;      // Ne pas oublier d'activer le buffer in#
    RPINR18bits.U1RXR = 13;     // Remap U1RX to RP13 
    
    // UART2 : UART PRINTER - Tx Pin only
    RPOR3bits.RP7R = 5;         // Remap U2TX to RP7
    
    // UART3 : HMI (COM)
    ANSBbits.ANSELB14 = 0;       // Ne pas oublier d'activer le buffer in#
    RPOR7bits.RP15R = 19;        // Remap U3TX to RP15
    RPINR17bits.U3RXR  = 14;     // Remap U3RX to RP14
    
    // UART4 : Coin Acceptor - Rx Pin only
    ANSBbits.ANSELB6 = 0;       // Ne pas oublier d'activer le buffer in#
    RPINR27bits.U4RXR = 6;      // Remap U4RX to RP6 
    
    
    // Config UART for com (HMI) (use #define COM_UART to specify UART3)
    com_init();
    
    // Config UART for GPS (use #define GPS_UART to specify UART1)
    gps_init();
    
    // Config UART for printer (use #define PRINTER_UART to specify UART2)
    printer_init();
    
    // Config UART for Coin acceptor (use #define COIN_UART to specify UART4)
    coinacc_init();
    
     
}

