/***************************************************************************
* Nom du prg 	:  
* Description	: 
*
* Auteur	: 
* Cr�� le	:
* Compilateur	: 
***************************************************************************
* Modifi� le  	:
***************************************************************************/


#include "lib_printer.h" // Inclusion du fichier .h "Applicatif" renomm�

/* Directives de compilation		*/


/* D�clarations des variables globales 	*/
const   uint8_t   PrintTestPage[]={PRN_DC2,PRN_PRINT_TEST_PAGE,0x00};

//------------------------------------------------------------------------------
/*	Impl�mentation du code */
//------------------------------------------------------------------------------
void    printer_init(void)
{
    // UART 19200 bps, most standard mode
    PRN_UXBRG = 51;        // 19200 bps avec BRGH=1, valeur 51 en th�orie
    PRN_UXMODE = 0x8008;
    PRN_UXSTA = 0x0400;
    
     __delay_ms(500);
    
     
   
     
    // Autorisation IRQ RX
    //PRN_RXIE = 1;
}
//------------------------------------------------------------------------------
void    printer_putch(uint8_t Byte)
{
    while(PRN_BFBIT); // wait while Tx buffer full
    PRN_UXTXREG = Byte;
}
//------------------------------------------------------------------------------
void    printer_puts(uint8_t *pStr)
{
    while (*pStr != '\0')
    {
        while (PRN_BFBIT); // wait while Tx buffer full
        PRN_UXTXREG = *pStr;
        pStr++;
    }
}
//------------------------------------------------------------------------------
void    printer_print_test_page(void)
{
    printer_puts((uint8_t*)PrintTestPage);
}
//------------------------------------------------------------------------------
void    printer_print(uint8_t *pStr)
{
    printer_puts(pStr);
    printer_putch(PRN_LF);
}
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------


