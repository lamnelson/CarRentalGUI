package carrental;

// imports
import java.sql.*;
import java.util.Scanner;

public class CarRental
{
    // create line for connection
    static Connection conn = null;
    // url string for db connection
    static String url = "jdbc:sqlite:C:/Users/14698/OneDrive/Desktop/CarRentalGUI/CarRentalDB.db";
    // statement for query
    static Statement st = null;
    static ResultSet rs = null;
    static String query = null;
    
    // function for db connection 
    public static boolean connect(Connection conn, String url) {
        boolean goodConn = false;
        // establish a connection with the database
        try {
            // establish a connection
            conn = DriverManager.getConnection(url);
            
            System.out.println("Connection to SQLite DB secured.");
            goodConn = true;
        } catch (SQLException e) {
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
        return goodConn;
    }
        
    public static void main(String[] args) throws SQLException {
        // call connection to db
        if (connect(conn, url)) {
            System.out.println("Welcome to the Car Rental Database");
            conn = DriverManager.getConnection(url);
        } else {
            System.exit(0);
        }
        
        // create scanner for input
        Scanner user = new Scanner(System.in);
        String line = null;
        String tableName = null;
        SQLquery(conn);
        // counter for program run
        Boolean run = true;
        while(run) {
            System.out.println("What table would you like to query?");
            System.out.println("1.\tCUSTOMER\n2.\tRATE\n3.\tRENTAL\n4.\tVEHICLE\n5.\tExit Program");
            line = user.nextLine();
            
            // check if user input == 1
            int check = Integer.valueOf(line.replaceAll("\\s", ""));
            switch (check)
            {
                case 1:
                    tableName = "CUSTOMER";
                    break;
                case 2:
                    tableName = "RATE";
                    break;
                case 3:
                    tableName = "RENTAL";
                    break;
                case 4:
                    tableName = "VEHICLE";
                    break;
                case 5:
                    run = false;
                    return;
                default:
                    System.out.println("Please re-enter only the numbers from the menu.");
                    continue;
            }
        }
    }
    
    public static String listColumn(Connection conn, Scanner user, String tableName) {
        int choice;
        boolean valid = true;
        try {
            query = "SELECT * FROM " + tableName;
            st = conn.createStatement();
            rs = st.executeQuery(query);
            ResultSetMetaData rsmd = (ResultSetMetaData) rs.getMetaData();
            int cols = rsmd.getColumnCount();
            String colName[] = new String[cols];
            System.out.println("What column would you like to update?");
            for (int i = 1; i <= cols; i++) {
                colName[i-1] = rsmd.getColumnLabel(i);
                System.out.format("%d: %s\n", i, colName[i-1]);
            }
            if (valid) {
                choice = Integer.valueOf((user.nextLine()).replaceAll("\\s", ""));
                if (choice < 0 || choice > cols) {
                    valid = false;
                } else {
                    valid = true;
                    return colName[choice + 1];
                }
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return "";
    }
    
    public static void updateQuery(Connection conn, Scanner user, String tableName) {
        System.out.println("What would you like to update from " + tableName);
        System.out.println("Please use SQL commands as your SET");
        boolean retry = true;
        while(retry) {
            String update = ((String) user.nextLine()).replaceAll("\n", "");
            query = "UPDATE " + tableName + " SET " + update;
            System.out.println("Does this look correct? 1 to try again");
            int choice = Integer.valueOf((user.nextLine()).replaceAll("\\s", ""));
            if(choice != 1) {
                retry = false;
            }
        }
        System.out.println("What is the requirement for the update");
        System.out.println("Please use SQL commands as your WHERE");
        retry = true;
        while(retry) {
            String requirement = ((String) user.nextLine()).replaceAll("\n", "");
            query += " WHERE " + requirement;
            System.out.println("Does this look correct? 1 to try again");
            int choice = Integer.valueOf((user.nextLine()).replaceAll("\\s", ""));
            if(choice != 1) {
                retry = false;
            }
        }
        System.out.println("Here is your final query: " + query);
        try {
            st = conn.createStatement();
            rs = st.executeQuery(query);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
    
    /*public static void SQLquery(Connection conn) {
        try {
            query = "SELECT * FROM RATE";
            st = conn.createStatement();
            rs = st.executeQuery(query);
            while(rs.next()) {
                int one = rs.getInt(1);
                int two = rs.getInt(2);
                int three = rs.getInt(3);
                int four = rs.getInt(4);
                System.out.format("%d %d %d %d\n", one, two, three, four);
            }
            st.close();
            rs.close();
        } catch (SQLException e) {
            System.out.println(e.getMessage() + "1");
        } catch (Exception ex) {
            System.out.println(ex.getMessage() + "2");
        }
    }*/
}
