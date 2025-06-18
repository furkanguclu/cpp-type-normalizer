# C/C++ Type Normalizer

Bu araç, C/C++ projelerinde kullanılan geleneksel veya platforma özel veri tiplerini, modern `<stdint.h>` tipleri ile otomatik olarak değiştirir.  
Hem güvenli (.bak yedekli), hem de proje çapında toplu çalışır.

## Özellikler

- .c, .cpp, .h, .hpp dosyalarında toplu tarama  
- Tip isimlerini güvenli biçimde (regex + kelime sınırı) değiştirme  
- Dosyaları orijinaliyle aynı klasörde .bak olarak yedekler  
- VSCode ile tam uyumlu .vscode/settings.json dosyası içerir  
- type_map.json ile kolayca genişletilebilir yapı

## Kurulum

1. Repoyu klonlayın veya zip olarak indirin:

git clone https://github.com/furkanguclu/cpp-type-normalizer.git
cd cpp-type-normalizer

2. Dosya yapısı:

.
├── convert_types.py       → Python dönüştürücü script  
├── type_map.json          → Eski → Yeni tip eşleştirmesi  
├── src/                   → Taranacak kaynak dosyalar  
└── .vscode/settings.json  → VSCode için yapılandırma

## Kullanım

1. Dönüştürmek istediğiniz .cpp, .h gibi dosyaları src/ klasörüne yerleştirin.  
2. Terminalde scripti çalıştırın:

python convert_types.py

3. Script:

- .c, .cpp, .h, .hpp uzantılı dosyaları tarar  
- Tip isimlerini belirlenen eşleştirmeye göre değiştirir  
- Orijinal dosyanın .bak uzantılı bir yedeğini oluşturur

## Örnek

Girdi (src/test.cpp):

DWORD id = 5;  
WORD port = 80;  
BYTE flag = 1;  
long long int big = 123456789LL;  
time_t now = time(nullptr);

Çıktı (src/test.cpp):

uint32_t id = 5;  
uint16_t port = 80;  
uint8_t flag = 1;  
int64_t big = 123456789LL;  
int32_t now = time(nullptr);

Ayrıca src/test.cpp.bak dosyası otomatik oluşturulur.

## Özelleştirme

Tüm tip eşleşmeleri type_map.json dosyasında tanımlıdır.  
Kendi özel tiplerinizi kolayca ekleyebilirsiniz:

{
  "DWORD": "uint32_t",
  "WORD": "uint16_t",
  "BYTE": "uint8_t",
  "long long int": "int64_t",
  "time_t": "int32_t"
}

## VSCode Uyumu

.vscode/settings.json dosyası sayesinde şu uzantılar C++ olarak tanınır:

{
  "files.associations": {
    "*.tpp": "cpp",
    "*.ipp": "cpp",
    "*.h": "cpp",
    "*.hpp": "cpp",
    "*.c": "c",
    "*.cpp": "cpp"
  }
}

## Lisans

MIT Lisansı altında dağıtılmaktadır.  
Açık kaynak, dilediğiniz gibi kullanabilir, kopyalayabilir, dağıtabilir ve katkı sağlayabilirsiniz.

Saygılarımla Furkan Güçlü




----------------------------------------------------------------------------------------------------------------------------------------------------------




C/C++ Type Normalizer
This tool automatically replaces traditional or platform-specific type definitions in C/C++ projects with modern <stdint.h> equivalents.
It works project-wide, safely creates .bak backups, and supports batch processing.

Features
Recursive scanning of .c, .cpp, .h, .hpp files

Safe replacement using regex with word boundaries

In-place modification with .bak file backups

Fully compatible with VSCode via .vscode/settings.json

Easily extendable via type_map.json

Installation
Clone the repository or download it as a zip:

git clone https://github.com/furkanguclu/cpp-type-normalizer.git
cd cpp-type-normalizer

Project structure:

.
├── convert_types.py → Python type conversion script
├── type_map.json → Legacy → Modern type mappings
├── src/ → Source files to be processed
└── .vscode/settings.json → VSCode configuration

Usage
Place the .cpp, .h, or other relevant files into the src/ directory.

Run the script from your terminal:

python convert_types.py

The script will:

Scan all .c, .cpp, .h, .hpp files

Replace types according to type_map.json

Create .bak backups for each modified file

Example
Input (src/test.cpp):

DWORD id = 5;
WORD port = 80;
BYTE flag = 1;
long long int big = 123456789LL;
time_t now = time(nullptr);

Output (src/test.cpp):

uint32_t id = 5;
uint16_t port = 80;
uint8_t flag = 1;
int64_t big = 123456789LL;
int32_t now = time(nullptr);

A backup file src/test.cpp.bak is automatically created.

Customization
All type mappings are defined in type_map.json.
You can easily add your own custom types:

{
"DWORD": "uint32_t",
"WORD": "uint16_t",
"BYTE": "uint8_t",
"long long int": "int64_t",
"time_t": "int32_t"
}

VSCode Compatibility
The .vscode/settings.json file ensures these file extensions are treated as C++:

{
"files.associations": {
".tpp": "cpp",
".ipp": "cpp",
".h": "cpp",
".hpp": "cpp",
".c": "c",
".cpp": "cpp"
}
}

License
Distributed under the MIT License.
You are free to use, modify, distribute, and contribute.

Respectfully,
Furkan Güçlü

