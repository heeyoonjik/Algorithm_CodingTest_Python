import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {
	public static void main(String [] args) throws NumberFormatException, IOException {
	   	 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	   	 int count = Integer.parseInt(br.readLine());
		int[][] arr = new int[count][2];
			for(int j=0; j<count; j++) {
				int[] intArr = new int [2];
	   	 		String[] str = br.readLine().split(" ");
				for(int k=0; k<2; k++) {
					arr[j][k] = Integer.parseInt(str[k]);
				}
			}
		
		   	 Arrays.sort(arr, (e1, e2) -> {
					if(e1[0] == e2[0]) {
						return e1[1] - e2[1];
					} else {
						return e1[0] - e2[0];
					}
				});
			
			for(int i=0; i<arr.length; i++) {
				for(int j=0; j<2; j++) {
					if(j==1) {
						System.out.print(arr[i][j]);
					}else {
						System.out.print(arr[i][j]+" ");
	
					}				}
				System.out.println();
			}
	}
}

 