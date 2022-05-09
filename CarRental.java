package carrental;

// imports
import java.sql.*;
import java.util.Scanner;

public class CarRental
{
    // create line for connection
    static Connection conn = null;
    // url string for db connection
    static String url = "";
    // statement for query
    static ResultSet rs;
    static String query = null;
    
    // function for db connection 
    public static int connect(Connection conn, String url) {
        
        // establish a connection with the database
        try {
            // establish a connection
            conn = DriverManager.getConnection(url);
            
            System.out.println("Connection to SQLite DB secured.");
            return 0;
        } catch (Exception e) {
            System.out.print(e.getMessage());
        } finally {
            try {
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException ex) {
                System.out.println(ex.getMessage());
            }
        }
        return 1;
    }
        
    public static void main(String[] args) throws SQLException {
        // call connection to db
        if (connect(conn, url) == 0) {
            System.out.println("Welcome to the Car Rental Database");
        } else {
            System.exit(0);
        }
        
        // create scanner for input
        Scanner user = new Scanner(System.in);
        String line = null;
        String tableName = null;
        
        // counter for program run
        int counter = 0;
        while(counter == 0) {
            System.out.println("What table would you like to query?");
            System.out.println("1.\tCUSTOMER\n2.\tRATE\n3.\tRENTAL\n4.\tVEHICLE\n5.\tExit Program");
            line = user.nextLine();
            
            // check if user input == 1
            int check = Integer.valueOf(line.replaceAll("\\s", ""));
            switch (check)
            {
                case 1 -> tableName = "CUSTOMER";
                case 2 -> tableName = "RATE";
                case 3 -> tableName = "RENTAL";
                case 4 -> tableName = "VEHICLE";
                case 5 ->
                {
                    counter = 1;
                    return;
                }
            }
        }
    }
}
