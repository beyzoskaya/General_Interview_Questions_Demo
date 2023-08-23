#include <set>
#include <vector>
using namespace std;

namespace SUIT {
enum Enum{
    SPADE,
    HEART,
    CLUB,
    DIAMOND
};
};

class Card{
private:
    SUIT::Enum s;
    int v;
public:
    virtual SUIT::Enum suit() const
    {
        return s;
    };
    virtual int val() const
    {
        return v;
    };

    Card(int val, SUIT::Enum suit)
    : s(suit), v(val){};
};

class BlackJackCard: public Card{
public:
    virtual int val()
    {
        int v = Card::val();
        if(v < 10)
            return v;
        return 10;
    }

    BlackJackCard(int val, SUIT::Enum suit)
        : Card(val,suit){};
};

class player {
private:
int id;
int bet;
set<int> points;
vector<BlackJackCard*> bjcs;
};