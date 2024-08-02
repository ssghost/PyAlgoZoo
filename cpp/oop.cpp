#include <iostream>

class Shape {
public:
    virtual void display();
};

class Rect: public Shape {void display();};

class Circ: public Shape {void display();};

void Rect::display(){};

void Circ::display(){}; 

int main() {
    Rect r;
    Circ c;
    Shape *s[2]={&r, &c};
    for (auto p: s) {
        p->display();
    }
}