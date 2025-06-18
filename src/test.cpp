// src/test.cpp
#include <iostream>
#include <ctime>

DWORD a = 123;
WORD b = 456;
BYTE c = 255;
long long int big = 123456789012345LL;
unsigned short port = 8080;
unsigned long id = 987654;
time_t now = time(nullptr);
size_t len = 1024;
INT counter = 42;
unsigned int flags = 0;
long long another_big = 1122334455;
short s = 12;
unsigned char byte = 100;
signed i = -1;

int main() {
    std::cout << "a = " << a << "\\n";
    std::cout << "b = " << b << "\\n";
    std::cout << "c = " << (int)c << "\\n";
    std::cout << "big = " << big << "\\n";
    std::cout << "port = " << port << "\\n";
    std::cout << "id = " << id << "\\n";
    std::cout << "now = " << now << "\\n";
    std::cout << "len = " << len << "\\n";
    std::cout << "counter = " << counter << "\\n";
    std::cout << "flags = " << flags << "\\n";
    std::cout << "another_big = " << another_big << "\\n";
    std::cout << "s = " << s << "\\n";
    std::cout << "byte = " << (int)byte << "\\n";
    std::cout << "i = " << i << "\\n";
    return 0;
}
