class Solution {
    public String intToRoman(int num) {
        StringBuilder roman = new StringBuilder();
        while (num > 0){
            if (num >= 1000){
                for (int i = 0; i < (num/1000); i++){
                    roman.append('M');
                }
                num = num - (num/1000) * 1000;
            }
            else if (num >= 900){
                roman.append("CM");
                num -= 900;
            }
            else if (num >= 500){
                for (int i = 0; i < (num/500); i++){
                    roman.append('D');
                }
                num = num - (num/500) * 500;
            }
            else if (num >= 400){
                roman.append("CD");
                num -= 400;
            }
            else if (num >= 100){
                for (int i = 0; i < (num/100); i++){
                    roman.append('C');
                }
                num = num - (num/100) * 100;
            }
            else if (num >= 90){
                roman.append("XC");
                num -= 90;
            }
            else if (num >= 50){
                for (int i = 0; i < (num/50); i++){
                    roman.append('L');
                }
                num = num - (num/50) * 50;
            }
            else if (num >= 40){
                roman.append("XL");
                num -= 40;
            }
            else if (num >= 10){
                for (int i = 0; i < (num/10); i++){
                    roman.append('X');
                }
                num = num - (num/10) * 10;
            }
            else if (num == 9){
                roman.append("IX");
                num -= 9;
            }
            else if (num >= 5){
                for (int i = 0; i < (num/5); i++){
                    roman.append('V');
                }
                num = num - (num/5) * 5;
            }
            else if (num == 4){
                roman.append("IV");
                num -= 4;
            }
            else{
                for (int i = 0; i < (num); i++){
                    roman.append('I');
                }
                num = num - num;
            }
        }
        return roman.toString();   
    }
}
