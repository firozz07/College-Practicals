public class Length2D {
    public static void main(String[] args) {
        int [][]arr={
            {1,2,3},
            {4,5,6},
            {7,8,9}
        };
        int rowSize=arr.length;
        int colSize=arr[0].length;
        for (int i = 0; i < rowSize; i++) {
            for (int j = 0; j < colSize; j++) {
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
}
