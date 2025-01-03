/***************************************************************************
* Nom du fichier:
* Description	: 
*
* Auteur	: 
* Créé le	:
* Compilateur	: 
***************************************************************************
* Modifié le  	:
***************************************************************************/

#include <xc.h>

//-----------------------------------------------------------------------------
#define COIN_UART   4
//-----------------------------------------------------------------------------
#if (COIN_UART == 1)
    #define COIN_UXBRG   U1BRG
    #define COIN_UXMODE  U1MODE
    #define COIN_UXSTA   U1STA
    #define COIN_BFBIT   U1STAbits.UTXBF
    #define COIN_UXTXREG U1TXREG
    #define COIN_RXIE    IEC0bits.U1RXIE 
    #define COIN_RXISR   _U1RXInterrupt 
    #define COIN_UXRXREG U1RXREG
    #define COIN_RXIF    IFS0bits.U1RXIF  
#elif (COIN_UART == 2)
    #define COIN_UXBRG   U2BRG
    #define COIN_UXMODE  U2MODE
    #define COIN_UXSTA   U2STA
    #define COIN_BFBIT   U2STAbits.UTXBF
    #define COIN_UXTXREG U2TXREG
    #define COIN_RXIE    IEC1bits.U2RXIE 
    #define COIN_RXISR   _U2RXInterrupt
    #define COIN_UXRXREG U2RXREG
    #define COIN_RXIF    IFS1bits.U2RXIF
#elif (COIN_UART == 3)
    #define COIN_UXBRG   U3BRG
    #define COIN_UXMODE  U3MODE
    #define COIN_UXSTA   U3STA
    #define COIN_BFBIT   U3STAbits.UTXBF
    #define COIN_UXTXREG U3TXREG
    #define COIN_RXIE    IEC5bits.U3RXIE 
    #define COIN_RXISR   _U3RXInterrupt
    #define COIN_UXRXREG U3RXREG
    #define COIN_RXIF    IFS5bits.U3RXIF
#elif (COIN_UART == 4)
    #define COIN_UXBRG   U4BRG
    #define COIN_UXMODE  U4MODE
    #define COIN_UXSTA   U4STA
    #define COIN_BFBIT   U4STAbits.UTXBF
    #define COIN_UXTXREG U4TXREG
    #define COIN_RXIE    IEC5bits.U4RXIE 
    #define COIN_RXISR   _U4RXInterrupt
    #define COIN_UXRXREG U4RXREG
    #define COIN_RXIF    IFS5bits.U4RXIF
#endif
//-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
/ Coin Values
/-----------------------------------------------------------------------------*/ 
typedef enum{
            NO_COIN=0,
            CENT10=1,
            CENT20=2,
            CENT50=5,
            EURO1=10,
            EURO2=20} tCoinValue;
//----------------------------------------------------------------------------
            
/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
void    coinacc_init(void);

/*--------------------------------------------------------------------------*/
/* Fonction  :  tCoinValue     coinacc_check(tCoinValue *pCoin)             */
/* Description : Vérifie si une pièce a été insérée dans le monnayeur       */
/* PE :                                                                     */
/* ps :   Valeur de la piece ou NO_COIN (cf tCoinValue)                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/
tCoinValue     coinacc_check(tCoinValue *pCoin);

/*--------------------------------------------------------------------------*/
/* Fonction  :  void    coinacc_clear(void);                                */
/* Description :  "Acquitte" le fait qu'une pièce ait été insérée.          */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi : A appeler après un coinacc_check "actif"                 */
/*--------------------------------------------------------------------------*/
void    coinacc_clear(void);


/*--------------------------------------------------------------------------*/
/* Fonction  :                                                              */
/* Description :                                                            */
/* PE :                                                                     */
/* ps :                                                                     */
/* Mode d'emploi :                                                          */
/*--------------------------------------------------------------------------*/





