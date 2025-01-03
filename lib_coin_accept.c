/***************************************************************************
* Nom du prg 	:  
* Description	: 
*
* Auteur	: 
* Crée le	:
* Compilateur	: 
***************************************************************************
* Modifi� le  	:
***************************************************************************/


#include "lib_coin_accept.h" // Inclusion du fichier .h "Applicatif" renomm�

/* Directives de compilation		*/


/* D�clarations des variables globales 	*/
uint8_t     CoinRxCar = 0;
tCoinValue  CoinValue = 0;

/*	Impl�mentation du code */
//----------------------------------------------------------------------------
void _ISR __attribute__((no_auto_psv)) COIN_RXISR(void)
{
    CoinRxCar = COIN_UXRXREG;
    
    if (CoinRxCar != 0xFF)      // get rid of strange 0xFF randomly sent by coin acceptor
    {
        switch (CoinRxCar)
        {
            case CENT10 : 
            case CENT20 :
            case CENT50:
            case EURO1:
            case EURO2: CoinValue = (tCoinValue)CoinRxCar;break;

            default : CoinValue = NO_COIN;break;
        }
    }
    
    COIN_RXIF = 0;
} // _InterruptVector
//----------------------------------------------------------------------------
void    coinacc_init(void)
{
    // UART 9600 bps, most standard mode
    COIN_UXBRG =    104;        // 9600 bps avec BRGH=1, valeur 103 en th�orie
    COIN_UXMODE =   0x8008;
    COIN_UXSTA =    0x0400;
    
    // Autorisation IRQ RX
    COIN_RXIE = 1;
}
//----------------------------------------------------------------------------
tCoinValue  coinacc_check(tCoinValue   *pCoin)
{
    *pCoin = CoinValue;
    return CoinValue;
}
//----------------------------------------------------------------------------
void    coinacc_clear(void)
{
    CoinValue = NO_COIN;
}
//----------------------------------------------------------------------------
//----------------------------------------------------------------------------
//----------------------------------------------------------------------------
//----------------------------------------------------------------------------
//----------------------------------------------------------------------------




