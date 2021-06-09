#include <iostream>
#include <map>

void print_hung_tien_in_map(const std::map<std::string, std::string>& input) {
  std::string license_plate = input.at("Hung-Tien Huang");
  std::cout << license_plate << std::endl;
}

int main(int argc, char** argv) {
  std::map<std::string, std::string> input{
      {std::pair<std::string, std::string>{"Hung-Tien Huang", "279-FR"},
       std::pair<std::string, std::string>{"Chien-Ping Wu", "KKA-0580"}}};
  print_hung_tien_in_map(input);
  return 0;
}