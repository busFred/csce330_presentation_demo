#include <iostream>
#include <map>
#include <vector>

void print_hung_tien_in_map(const std::map<std::string, std::string>& input) {
  std::string license_plate = input.at("Hung-Tien Huang");
  std::cout << license_plate << std::endl;
}

int main(int argc, char** argv) {
  std::vector<std::string> input{"Hung-Tien Huang", "Chien-Ping, Wu"};
  print_hung_tien_in_map(input);
  return 0;
}