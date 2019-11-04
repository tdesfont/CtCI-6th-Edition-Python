#include <iostream>
using namespace std;

#define NAME_SIZE 50 // Point de syntaxe important

class Person {
    int id;
    char name[NAME_SIZE];

public:
    void aboutMe(){
        cout << "I am a person";
    }
};

class Student : public Person {
public:
    void aboutMe() {
        cout << "I am a student.";
    }
};

int main() {
    Student * p = new Student();
    p->aboutMe();
    delete p;
    return 0;
}