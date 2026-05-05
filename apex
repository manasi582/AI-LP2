Click developer console in the gear box on the right
Then create new apex class

public class Sample {
    public static void addNumbers() {
        Integer num1 = 10;
        Integer num2 = 20;

        Integer sum = num1 + num2;
        System.debug('sum of two numbers is: ' + sum);
    }
}

Then execute this:
Sample.addNumbers();
