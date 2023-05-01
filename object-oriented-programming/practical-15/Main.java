class Main {
    public static void main(String[] args) {
         System.out.println(Main.binaryToDecimal("0101"));
    }
    public static int binaryToDecimal(String s) throws NumberFormatException {
        int decimal = 0;
        int last_index = s.length() - 1;
        int multiplier = 1;
        for (int i = 0; i <= last_index; i++) {
            char c = s.charAt(last_index - i);
            if (c == '1') {
                decimal += multiplier;
            }
            else if (c != '0') {
                throw new NumberFormatException("got error at index" + (last_index - i));
            }
            multiplier *= 2;
        }
        return decimal;
    }
}