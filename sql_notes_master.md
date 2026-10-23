# **Day 1\.**

# **SQL Notes: Examples to CREATE and DROP Tables**

## **1\. CREATE TABLE Statement**

* **General Syntax:**  
* 

SQL  
CREATE TABLE TableName (  
    COLUMN1 datatype,  
    COLUMN2 datatype,  
    COLUMN3 datatype,  
    ...  
);

* **Example 1 (Basic Table):** Creating a table named TEST that has 2 columns (ID and NAME):  
* 

SQL  
CREATE TABLE TEST (  
    ID int,  
    NAME varchar(30)  
);

* **Example 2 (Multiple Columns):** Creating a COUNTRY table that has ID, Country Code (CCODE), and Name:  
* 

SQL  
CREATE TABLE COUNTRY (  
    ID int,  
    CCODE char(2),  
    Name varchar(60)  
);

## **2\. Adding Constraints (Primary Key & NOT NULL)**

* If we do not want any duplicate records in a table, we make one column a PRIMARY KEY.  
*   
* **Industry Rule:** A database does not allow NULL (empty) values in any Primary Key. Therefore, it is necessary to add the NOT NULL constraint when defining the column.  
*   
* **Example 3 (Table with Primary Key):**  
* 

SQL  
CREATE TABLE COUNTRY (  
    ID int NOT NULL,  
    CCODE char(2),  
    Name varchar(60),  
    PRIMARY KEY (ID)  
);

## **3\. DROP TABLE Statement**

* **Work:** To permanently delete an existing table from the database.  
*   
* **General Syntax:**  
* 

SQL  
DROP TABLE TableName;

* **Real-World Scenario:** If you are creating a new table and a table with that name already exists in the database, you will get a table XXX.YYY already exists error.  
*   
* To avoid this error, it is a common practice in test and development environments to DROP the old table before creating the new table.  
*   
* **Example:**  
* 

SQL  
DROP TABLE COUNTRY;

CREATE TABLE COUNTRY (  
    ID int NOT NULL,  
    CCODE char(2),  
    Name varchar(60),  
    PRIMARY KEY (ID)  
);

* **Warnings (Things to keep in mind):**  
* 

  * Before dropping a table, make sure that it does not contain any important data that would be difficult to recover.  
  *   
  * If the table does not exist and you try to drop it, you will get an XXX.YYY is an undefined name error. If the CREATE statement runs successfully right after this, you can ignore this error.

# **Day 2\.**

# **Relational Model Constraints \- Data Integrity Notes**

In any well-designed database, **Data Integrity** is very important to maintain the accuracy, consistency, and reliability of the stored information. For this, three key relational model constraints are used: **Entity Integrity**, **Referential Integrity**, and **Domain Integrity**.

## **1\. Entity Integrity Constraint (Primary Key Rule)**

* **Work:** This constraint ensures that every table in the database has a Primary Key.  
*   
* **Rules for Primary Key:**  
* 

  1. This column can never be NULL (empty).  
  2.   
  3. Every value in this column must be **Unique** across the entire table.  
  4.   
* **Benefit:** It prevents duplication and missing identifiers, making every record (entity) distinct and identifiable.  
*   
* **Example Code:**  
* 

SQL  
CREATE TABLE BookShop (  
    BOOK\_ID INT PRIMARY KEY,  
    TITLE VARCHAR(100),  
    AUTHOR\_ID INT  
);

*(Here,* BOOK\_ID *is unique, meaning no two books can have the same ID, and it cannot be* NULL*.)*

## **2\. Referential Integrity Constraint (Foreign Key Rule)**

* **Work:** This constraint ensures that a Foreign Key in one table always refers to a valid Primary Key in another table.  
*   
* **Benefit:** It maintains a logical link between related data across different tables and prevents "orphaned" (invalid) references.  
*   
* **Example Code:**  
* 

SQL  
\-- Parent Table  
CREATE TABLE BookShop\_AuthorDetails (  
    AUTHOR\_ID INT PRIMARY KEY,  
    AUTHOR\_NAME VARCHAR(100)  
);

\-- Child Table  
CREATE TABLE BookShop (  
    BOOK\_ID INT PRIMARY KEY,  
    TITLE VARCHAR(100),  
    AUTHOR\_ID INT,  
    FOREIGN KEY (AUTHOR\_ID) REFERENCES BookShop\_AuthorDetails(AUTHOR\_ID)  
);

*(Explanation: A book cannot be inserted into the* BookShop *table if its* AUTHOR\_ID *does not exist in the* BookShop\_AuthorDetails *table.)*

## **3\. Domain Integrity Constraint (Data Validation Rules)**

* **Work:** This constraint ensures that the value stored in a column falls within its defined domain (rules). This includes Data type, Format, Allowed values, and Nullability.  
*   
* **Key Mechanisms used:**  
* 

  * **CHECK Constraint:** Sets logic on the range or pattern of a column's value (for example, Price cannot be negative).  
  *   
  * **NOT NULL Constraint:** Ensures that the column must have a value (it cannot be left empty).  
  *   
* **Example Code:**  
* 

SQL  
CREATE TABLE BookShop (  
    BOOK\_ID INT PRIMARY KEY,  
    TITLE VARCHAR(100) NOT NULL,  
    PRICE DECIMAL(5, 2) CHECK (PRICE \>= 0),  
    PUBLISHED\_DATE DATE  
);

*(Explanation: The* TITLE *column cannot be empty (*NOT NULL*), and the value of* PRICE *must be 0 or greater (*CHECK *constraint).)*

# **Understanding Relational Model Constraints (Data Integrity)**

In a well-designed database, **Data Integrity** is very important to maintain the accuracy, consistency, and reliability of stored information. To achieve this, three main constraints are used:

### **Sample Tables (For Context)**

We will use these two tables in the examples:

**1\. BookShop Table**

| BOOK\_ID | TITLE | AUTHOR\_ID |
| :---- | :---- | :---- |
| 1 | The Silent Patient | 101 |
| 2 | Educated | 102 |
| 3 | 1984 | 103 |
| 4 | To Kill a Mockingbird | 104 |
| 5 | The Great Gatsby | 105 |

**2\. BookShop\_AuthorDetails Table**

| AUTHOR\_ID | AUTHOR\_NAME |
| :---- | :---- |
| 101 | Alex Michaelides |
| 102 | Tara Westover |
| 103 | George Orwell |
| 104 | Harper Lee |
| 105 | F. Scott Fitzgerald |

## **1\. Entity Integrity Constraint (Primary Key Rule)**

* **Concept:** This constraint ensures that every table in a relational database must have a Primary Key.  
*   
* **Rules:** A primary key uniquely identifies any row.  
* 

  * Must **NOT** contain NULL values (can never be empty).  
  *   
  * Must be unique across all rows.  
  *   
* **Benefit:** It prevents data duplication and missing identifiers.  
*   
* **Example Code:**  
* 

SQL  
CREATE TABLE BookShop (  
    BOOK\_ID INT PRIMARY KEY,  
    TITLE VARCHAR(100),  
    AUTHOR\_ID INT  
);

*(Explanation: Here,* BOOK\_ID *is unique and cannot be* NULL*.)*

## **2\. Referential Integrity Constraint (Foreign Key Rule)**

* **Concept:** This constraint ensures that a Foreign Key in one table always refers to a valid Primary Key in another table.  
*   
* **Benefit:** It enforces a logical link between related data and prevents invalid or "orphaned" references from entering.  
*   
* **Example Code:**  
* 

SQL  
CREATE TABLE BookShop (  
    BOOK\_ID INT PRIMARY KEY,  
    TITLE VARCHAR(100),  
    AUTHOR\_ID INT,  
    FOREIGN KEY (AUTHOR\_ID) REFERENCES BookShop\_AuthorDetails(AUTHOR\_ID)  
);

*(Explanation: Only an* AUTHOR\_ID *that is already present in* BookShop\_AuthorDetails *can be inserted into* BookShop*. If you try to insert a book whose author does not exist, an error will occur.)*

## **3\. Domain Integrity Constraint (Data Validation Rules)**

* **Concept:** This ensures that the value stored in a column falls within its defined domain (rules).  
*   
* **It includes rules about:** Data type, Format, Allowed values, and Nullability.  
*   
* **Standard Mechanisms Used:**  
* 

  1. **CHECK Constraint:** Sets the range or pattern of acceptable values in a column. (For example: PRICE \>= 0 checks that the price is not negative).  
  2.   
  3. **NOT NULL Constraint:** Ensures that the column must contain a value; it cannot be left empty (NULL). (For example: TITLE is mandatory).  
  4.   
* **Example Code:**  
* 

SQL  
CREATE TABLE BookShop (  
    BOOK\_ID INT PRIMARY KEY,  
    TITLE VARCHAR(100) NOT NULL,  
    PRICE DECIMAL(5, 2) CHECK (PRICE \>= 0),  
    PUBLISHED\_DATE DATE  
);

# 

# **Day 3\.**

# **Advanced SELECT Queries: LIKE, BETWEEN, and IN**

When we do not know the exact value in the WHERE clause, or when the query is becoming too long, we use these three techniques.

## **1\. String Patterns (LIKE Operator)**

* **Work:** Used to search for a specific text pattern in a column.  
*   
* **Wildcard Character (**%**):** The % (percent sign) is used to substitute (replace) missing characters. It can be placed before, after, or on both sides of the pattern.  
*   
* **Example Scenario:** We do not remember the exact name of the author; we only remember that the name starts with 'R'.  
*   
* **Query:**  
* 

SQL  
SELECT firstname FROM author WHERE firstname LIKE 'R%';

**Concept Output (Author Table):**

| firstname |
| :---- |
| Raul |
| Rav |

*(Only those rows will be returned whose name starts with R.)*

## **2\. Ranges (BETWEEN ... AND Operator)**

* **Work:** To filter values that fall within a range (inclusive of both start and end values).  
*   
* **Benefit:** It makes long conditions using \>= (greater than or equal to) and \<= (less than or equal to) shorter and easier.  
*   
* **Example Scenario:** Retrieving books whose pages are between 290 and 300\.  
*   
* **Query:**  
* 

SQL  
\-- Normal way (Long method):  
\-- WHERE pages \>= 290 AND pages \<= 300

\-- Smart way (BETWEEN operator):  
SELECT \* FROM Book WHERE pages BETWEEN 290 AND 300;

## **3\. Sets of Values (IN Operator)**

* **Work:** To specify multiple exact values (a set of values) together in the WHERE clause.  
*   
* **Benefit:** When data cannot be grouped into ranges (like text values), we use IN to avoid writing OR repeatedly.  
*   
* **Example Scenario:** We want data for authors who are from 'Australia' or 'Brazil'. If we also add Canada, India, and China, the OR condition will become very long.  
*   
* **Query:**  
* 

SQL  
\-- Without the IN operator (Long method):  
\-- WHERE country \= 'Australia' OR country \= 'Brazil'

\-- Smart way (IN operator):  
SELECT \* FROM author WHERE country IN ('Australia', 'Brazil');

These are used the most in the real world to filter data\!

# **Day 4\.**

# **SQL Notes: Sorting Result Sets (ORDER BY)**

When retrieving data using the SELECT statement, the results are not automatically sorted. To display the result set in a specific, organized way (like alphabetical or numerical order), we use the ORDER BY clause.

## **1\. Default Sorting (Ascending Order)**

* **Rule:** By default, the ORDER BY clause sorts data in Ascending order (A to Z, or lowest to highest number).  
*   
* **Example Scenario:** You want a list of book titles arranged alphabetically.  
*   
* **Query:**  
* 

SQL  
SELECT title FROM book   
ORDER BY title;

**Conceptual Output Table:**

| title (Sorted A-Z) |
| :---- |
| A Tale of Two Cities |
| Harry Potter |
| The Great Gatsby |
| To Kill a Mockingbird |

## **2\. Descending Sorting (DESC Keyword)**

* **Rule:** To sort data in reverse order (Z to A, or highest to lowest number), you must add the DESC keyword at the end of the clause.  
*   
* **Sorting Logic (Ties):** If the first few words of the data are exactly the same, the database checks character by character until it finds a difference to determine the order.  
*   
* **Query:**  
* 

SQL  
SELECT title FROM book   
ORDER BY title DESC;

**Conceptual Output Table:**

| title (Sorted Z-A) |
| :---- |
| To Kill a Mockingbird |
| The Great Gatsby |
| Harry Potter |
| A Tale of Two Cities |

## **3\. Sorting by Column Sequence Number (Index)**

* **Rule:** Instead of typing the full column name in the ORDER BY clause, you can just use its sequence number (its position in your SELECT list).  
*   
* **Benefit:** This saves time and makes the query shorter to write.  
*   
* **Example Scenario:** You select title (column 1\) and pages (column 2\) and want to sort the results by the number of pages (lowest to highest).  
*   
* **Query:**  
* 

SQL  
SELECT title, pages FROM book   
ORDER BY 2; 

*(Explanation: Here,* 2 *represents the* pages *column because it is the second item listed after* SELECT*.)*

**Conceptual Output Table:**

| title (Column 1\) | pages (Column 2 \- Sorted Lowest to Highest) |
| :---- | :---- |
| The Great Gatsby | 180 |
| To Kill a Mockingbird | 281 |
| A Tale of Two Cities | 341 |
| Harry Potter | 500 |

# 

# **Day 5\.**

# **SQL Notes: Grouping and Filtering Result Sets**

Sometimes, simply retrieving data is not enough; we need to summarize it, count it, and filter the grouped results. We use DISTINCT, GROUP BY, and HAVING clauses for this.

## **1\. Eliminating Duplicates (DISTINCT)**

* **Rule:** If a column contains repeated values and you only want to see the unique values, use the DISTINCT keyword.  
*   
* **Example Scenario:** The author table has 20 authors from 6 different countries. If you just select country, you get 20 rows (with duplicates).  
*   
* **Query:**  
* 

SQL  
SELECT DISTINCT country FROM author   
ORDER BY 1;

**Conceptual Output Table:**

| country (Unique List) |
| :---- |
| Australia |
| Brazil |
| Canada |
| China |
| India |
| USA |

## **2\. Grouping Data & Counting (GROUP BY)**

* **Rule:** The GROUP BY clause groups rows that have the same values into summary rows. It is almost always used with aggregate functions like COUNT(), SUM(), or AVG().  
*   
* **Example Scenario:** You want to know how many authors come from each country.  
*   
* **Query:**  
* 

SQL  
SELECT country, COUNT(country)   
FROM author   
GROUP BY country;

## **3\. Renaming Columns (AS Keyword / Aliasing)**

* **Rule:** When you use a function like COUNT(), the database might give the column an ugly default name (like "2" or "COUNT(country)"). Use the AS keyword to give the column a clean, readable name.  
*   
* **Query:**  
* 

SQL  
SELECT country, COUNT(country) AS Count   
FROM author   
GROUP BY country;

**Conceptual Output Table:**

| country | Count |
| :---- | :---- |
| Australia | 2 |
| Canada | 3 |
| China | 6 |
| India | 6 |
| USA | 3 |

## **4\. Filtering Grouped Data (HAVING Clause)**

* **Rule:** If you want to filter data after it has been grouped, you must use the HAVING clause.  
*   
* **⚠️ Crucial Interview Tip (WHERE vs. HAVING):**  
* 

  * WHERE filters individual rows **before** grouping.  
  *   
  * HAVING filters grouped rows/aggregates **after** grouping.  
  *   
* **Example Scenario:** Show only the countries that have more than 4 authors.  
*   
* **Query:**  
* 

SQL  
SELECT country, COUNT(country) AS Count   
FROM author   
GROUP BY country   
HAVING COUNT(country) \> 4;

**Conceptual Output Table:**

| country | Count |
| :---- | :---- |
| China | 6 |
| India | 6 |

# **Day 6\.**

# **SQL Notes: Built-in Database Functions**

### **Sample Table for Context: PETRESCUE**

| ID | ANIMAL | QUANTITY | COST | RESCUE\_DATE |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Cat | 1 | 450.00 | 2026-05-11 |
| 2 | Dog | 3 | 1200.00 | 2026-06-15 |

## **1\. Aggregate (Column) Functions**

* **Work:** These functions take a whole column of values (a collection of like values) as input and return a single value (or NULL).  
*   
* **Common Functions & Examples:**  
* 

  1. SUM()**:** Adds all the values in a column.  
  2. 

  3. SQL

SELECT SUM(COST) FROM PETRESCUE;

4.   
   5.   
   6. MAX() **&** MIN()**:** To find the Highest and Lowest values.  
   7. 

   8. SQL

SELECT MAX(QUANTITY) FROM PETRESCUE;  
SELECT MIN(ID) FROM PETRESCUE WHERE ANIMAL \= 'Dog';

9.   
   10.   
   11. AVG()**:** Calculates the average (mean) value.  
   12. 

   13. SQL

SELECT AVG(COST) FROM PETRESCUE;

14.   
    15.   
* **Pro-Tips for Aggregate Functions:**  
* 

  1. **Aliasing (**AS **Keyword):** When we run an aggregate function, the name of the output column can be a strange number or expression. To make it readable, we use AS:  
  2. 

  3. SQL

SELECT SUM(COST) AS SUM\_OF\_COST FROM PETRESCUE;

4.   
   5.   
   6. **Math Operations Inside Functions:** You can also perform direct math calculations inside functions. (Example: Finding the per-unit cost of each dog):  
   7. 

   8. SQL

SELECT AVG(COST / QUANTITY) FROM PETRESCUE WHERE ANIMAL \= 'Dog';

9.   
   10. 

## **2\. Scalar & String Functions**

* **Work:** These functions operate on every individual value (row-by-row) of a column.  
*   
* **Common Functions & Examples:**  
* 

  1. ROUND()**:** Rounds numeric values up or down to the nearest integer.  
  2. 

  3. SQL

SELECT ROUND(COST) FROM PETRESCUE;

4.   
   5.   
   6. LENGTH()**:** Tells the length of the string (number of characters).  
   7. 

   8. SQL

SELECT LENGTH(ANIMAL) FROM PETRESCUE;

9.   
   10.   
   11. UPPERCASE() **&** LOWERCASE() **(or** UCASE() **/** LCASE()**):** Converts text into capital or small letters.  
   12. 

   13. SQL

SELECT UPPERCASE(ANIMAL) FROM PETRESCUE;

  
* **Pro-Tips for Scalar Functions:**  
* 

  1. **Using in WHERE Clause (Smart Filtering):** If you do not know whether 'Cat', 'CAT', or 'cat' is written in the database, convert the data into lowercase and then compare it. This trick is very useful in real-world data cleaning\!  
  

  2. SQL

SELECT \* FROM PETRESCUE WHERE LOWERCASE(ANIMAL) \= 'cat';
   
   3.   
   4. **Nesting Functions:** You can put the output of one function inside another function. (Example: You want unique animal names in uppercase):  
    

   5. SQL

SELECT DISTINCT(UPPERCASE(ANIMAL)) FROM PETRESCUE;

 

# 

# **Day 7\.**

# **SQL Notes: Date and Time Functions**

Most databases have special data types to store and manage dates and times. These functions are critical for creating time-series reports in real-world Data Analytics.

## **1\. SQL Date and Time Data Types**

* DATE**:** Has 8 digits, formatted as YYYYMMDD.  
    
* TIME**:** Has 6 digits, formatted as HHMMSS.  
    
* TIMESTAMP**:** Has 20 digits, formatted as YYYYXXDDHHMMSSZZZZZZ.  
  

  * XX represents the month.  
     
  * ZZZZZZ represents microseconds.  
   

### **Sample Table for Context: PETRESCUE**

*(A conceptual table to understand the queries below)*

| ID | ANIMAL | QUANTITY | COST | RESCUE\_DATE |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Cat | 1 | 450.00 | 2026-05-11 |
| 2 | Dog | 3 | 1200.00 | 2026-06-15 |
| 3 | Cat | 2 | 800.00 | 2026-05-20 |

## **2\. Extracting Parts of a Date**

* **Work:** SQL has built-in functions to extract specific parts of a date, such as DAY(), MONTH(), WEEK(), HOUR(), MINUTE(), and SECOND().  
   
* **Example Scenario:** Extract only the day portion from the rescue dates for cats.  
 

SQL  
SELECT DAY(RESCUE\_DATE)   
FROM PETRESCUE   
WHERE ANIMAL \= 'Cat';

*(Output conceptual result:* 11, 20*)*

## **3\. Using Date Functions in the WHERE Clause**

* **Work:** You can filter your data by extracting a specific time period directly inside the WHERE clause.  
   
* **Example Scenario:** Find the total number of rescues that happened in the month of May (Month 5).  
 

SQL  
SELECT COUNT(\*)   
FROM PETRESCUE   
WHERE MONTH(RESCUE\_DATE) \= 5;

## **4\. Date and Time Arithmetic**

* **Work:** You can perform mathematical operations on dates (like adding or subtracting days) using functions like DATE\_ADD().  
   
* **Example Scenario:** Orders must be processed within 3 days. Find the exact date that is 3 days after each rescue date.  
 

SQL  
SELECT DATE\_ADD(RESCUE\_DATE, INTERVAL 3 DAY)   
FROM PETRESCUE;

## **5\. Special Registers (Current Date/Time)**

* **Work:** SQL provides special registers like CURRENT\_DATE and CURRENT\_TIME to get the exact system date and time right now.  
   
* **Example Scenario:** Calculate how much time has passed from each rescue date until today.  
 

SQL  
SELECT CURRENT\_DATE \- RESCUE\_DATE   
FROM PETRESCUE;

*(Note: The result of this arithmetic is typically returned in a format of years, months, and days).*

# **Day 8\.**

# **SQL Notes: Subqueries (Nested Queries)**

## **What is a Subquery?**

* A subquery (or nested query) is a regular SQL query placed inside parentheses () and embedded within another main (outer) query.  
   
* It helps bypass the limitations of basic SQL commands to form more powerful queries.  
 

### **Sample Table for Context: EMPLOYEES**

*(A conceptual table to understand the examples)*

| EMP\_ID | FIRST\_NAME | LAST\_NAME | SALARY | DEPT\_ID | DOB |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 101 | John | Doe | 60000 | D1 | 1990-05-14 |
| 102 | Alice | Smith | 80000 | D2 | 1985-08-21 |
| 103 | Bob | Martin | 50000 | D1 | 1992-11-03 |

## **1\. Subquery in the WHERE Clause (Filtering by Aggregates)**

* **The Problem:** We cannot directly use aggregate functions (like AVG(), MAX()) in a WHERE clause.  
 

  * **Error Example:** SELECT \* FROM employees WHERE salary \> AVG(salary); ❌ *(Invalid use of aggregate function)*  
     
* **The Solution:** Use a subquery to calculate the average first, and let the outer query compare against that result.  
   
* **Query Example:** *(Retrieve employees whose salary is less than the average salary)*  
 

SQL  
SELECT EMP\_ID, FIRST\_NAME, LAST\_NAME, SALARY   
FROM EMPLOYEES   
WHERE SALARY \< (SELECT AVG(SALARY) FROM EMPLOYEES);

## **2\. Subquery in the List of Columns (Column Expressions)**

* **The Problem:** If you want to compare individual row data with aggregate data (like each employee's salary vs. company average), a normal query will throw a GROUP BY error.  
 

  * **Error Example:** SELECT EMP\_ID, SALARY, AVG(SALARY) FROM EMPLOYEES; ❌ *(Missing GROUP BY clause)*  
  *   
* **The Solution:** Place the subquery directly inside the SELECT column list. It calculates the average independently for every row.  
   
* **Query Example:**  
 

SQL  
SELECT EMP\_ID, SALARY,   
       (SELECT AVG(SALARY) FROM EMPLOYEES) AS AVG\_SALARY   
FROM EMPLOYEES;

**Conceptual Output:**

| EMP\_ID | SALARY | AVG\_SALARY |
| :---- | :---- | :---- |
| 101 | 60000 | 63333 |
| 102 | 80000 | 63333 |

## **3\. Subquery in the FROM Clause (Derived Tables)**

* **The Concept:** Sometimes called Table Expressions or Derived Tables. Here, the outer query treats the result of the subquery as a temporary, virtual table.  
   
* **Real-world Use Case:** Great for data security (e.g., hiding sensitive columns like DOB or SALARY before doing further joins/analysis).  
   
* **Query Example:** *(Create a derived table with only non-sensitive information)*  
 

SQL  
SELECT \* FROM   
    (SELECT EMP\_ID, FIRST\_NAME, LAST\_NAME, DEPT\_ID   
     FROM EMPLOYEES) AS EMP4ALL;

*(Note:* EMP4ALL *is the temporary alias name given to the derived table).*

# **Day 9\.**

# **SQL Notes: Accessing Multiple Tables (Sub-queries & Implicit Joins)**

When data is scattered across multiple tables, we can access it using three main methods: **Sub-queries**, **Implicit Joins**, and **Join Operators** (like INNER/OUTER JOIN). This note covers the first two.

### **Sample Tables for Context**

**1\. EMPLOYEES Table**

| EMP\_ID | FIRST\_NAME | LAST\_NAME | SALARY | DEP\_ID |
| :---- | :---- | :---- | :---- | :---- |
| E101 | John | Doe | 60000 | D1 |
| E102 | Alice | Smith | 75000 | D2 |

**2\. DEPARTMENTS Table**

| DEP\_ID\_DEP | DEP\_NAME | MANAGER\_ID | LOC\_ID |
| :---- | :---- | :---- | :---- |
| D1 | IT | M01 | L0001 |
| D2 | Sales | M02 | L0002 |

## **1\. Using Sub-queries with Multiple Tables**

* **Work:** Using the result of one table's query as an input (filter) for another table's query.  
   
* **Example 1 (Basic Filter):** Retrieve employee records only if their department actually exists in the DEPARTMENTS table.  
 

SQL  
SELECT \* FROM employees   
WHERE DEP\_ID IN (SELECT DEP\_ID\_DEP FROM departments);

* **Example 2 (Filtering by another table's attribute):** Get employees working in a specific location (L0002). Location details are not in the employee table, so we use a sub-query on the departments table.  
 

SQL  
SELECT \* FROM employees   
WHERE DEP\_ID IN (SELECT DEP\_ID\_DEP FROM departments WHERE LOC\_ID \= 'L0002');

* **Example 3 (Reverse Dependency):** Find the Department ID and Department Name for departments where employees earn more than \$70,000.  
 

SQL  
SELECT DEP\_ID\_DEP, DEP\_NAME FROM departments   
WHERE DEP\_ID\_DEP IN (SELECT DEP\_ID FROM employees WHERE SALARY \> 70000);

## **2\. Implicit Joins (Multiple Tables in the FROM Clause)**

* **Work:** Specifying more than one table in the FROM clause separated by a comma ,.  
   
* **The Full Join (Cartesian Product) Warning:** If you simply run SELECT \* FROM employees, departments;, every row of the first table will join with every row of the second table, making the result set huge and useless.  
   
* **Fixing it with WHERE (Matching IDs):** For a proper implicit join, we have to link them on their common ID (Primary/Foreign Key).  
 

SQL  
SELECT \* FROM employees, departments   
WHERE employees.DEP\_ID \= departments.DEP\_ID\_DEP;

*(Note: We prefix the table name before the column name like* table.column *so that there is no ambiguity).*

* **Using Table Aliases (Best Practice):** Typing table names repeatedly can be long. We can give short nicknames (Aliases) to tables in the FROM clause.  
 

SQL  
SELECT E.EMP\_ID, D.DEP\_NAME   
FROM employees E, departments D   
WHERE E.DEP\_ID \= D.DEP\_ID\_DEP;

*(Explanation: Here* employees *became* E *and* departments *became* D*. This makes the code clean and professional.)*

# **Day 10\.**

# **SQL Notes: Accessing Databases with Python & SQL APIs**

As a Data Analyst, we use Python to connect to databases, run SQL queries, and analyze the data all in one place (usually inside a Jupyter Notebook).

## **1\. Why use Python for Database Access?**

* **Rich Ecosystem:** Has powerful data science libraries (NumPy, Pandas, Matplotlib, SciPy).  
   
* **Easy & Portable:** Simple syntax, open-source, and runs on any operating system without changing the code.  
   
* **DB-API:** Python has a standard Database API (DB-API) that makes writing database code very easy and well-documented.  
 

## **2\. Jupyter Notebooks (The Workspace)**

* **What is it?** A virtual web-based editor to create and share documents containing live code, visualizations, equations, and text.  
   
* **Key Advantages:**  
 

  * **Multi-language:** Supports 40+ languages (Python, R, Julia, Scala).  
     
  * **Easy Sharing:** Share easily via Email, Dropbox, or GitHub.  
     
  * **Rich Output:** Displays interactive HTML, images, videos, and LaTeX directly.  
     
  * **Big Data Integration:** Works seamlessly with tools like Apache Spark, Pandas, scikit-learn, and TensorFlow.  
   

## **3\. How Python Talks to Databases (API Workflow)**

An API (Application Programming Interface) is a set of functions that allows different software programs to talk to each other.  
When your Python code runs an SQL query, it follows a standard 4-step API workflow:

1. **Connect:** The program makes an API call to connect to the Database Management System (DBMS).  
   
2. **Build & Send:** The program builds the SQL query as a text string in a buffer, and makes an API call to pass this text to the DBMS.  
   
3. **Check Status:** It makes API calls to retrieve the query results, check the request status, and handle any errors.  
   
4. **Disconnect:** Finally, it makes an API call to close the connection to the database.  
 

## **4\. Popular Database APIs (Important Table)**

Every major database system uses its own specific proprietary API library to connect with applications. You must remember these pairings:

| Database System / Platform | SQL API / Library Used |
| :---- | :---- |
| MySQL | MySQL C API |
| PostgreSQL | psycopg2 |
| IBM DB2 | IBM\_DB |
| Microsoft SQL Server | dblib |
| Oracle | OCI |
| Microsoft Windows OS (General) | ODBC |
| Java Applications | JDBC |

# 

# **Day 11\.**

# **SQL Notes: Writing Code Using Python DB-API**

## **1\. What is Python DB-API?**

* **Definition:** It is the standard Application Programming Interface (API) for accessing relational databases in Python.  
    
* **Core Benefit:** Write your database code once. Instead of learning a completely new way to code for every different database, DB-API provides a single, standard structure that works across multiple relational databases.  
    
* **Advantages:** Easy to understand, ensures consistency across different Python modules, highly portable code, and provides broad database connectivity.  
  

## **2\. DB-API Libraries for Popular Databases**

Every database system uses its own specific library to connect to Python applications.

| Database System | Python DB-API Library |
| :---- | :---- |
| IBM DB2 | ibm\_db |
| MySQL | mysql-connector-python |
| PostgreSQL | psycopg2 |
| MongoDB | PyMongo |

## **3\. The Two Main Concepts: Connections vs. Cursors**

### **A. Connection Objects**

* **Purpose:** Used to connect to the database and manage transactions.  
    
* **Key Methods associated with Connections:**  
 

  1. cursor(): Creates and returns a new cursor object using the active connection.  
  2.   
  3. commit(): Saves (commits) any pending transactions or changes to the database.  
  4.   
  5. rollback(): Undoes any pending transactions, rolling the database back to its state before the transaction started.  
  6.   
  7. close(): Closes the database connection to free up system resources.  
  8. 

### **B. Cursor Objects (Query Objects)**

* **Purpose:** Used to run SQL queries and scan/scroll through the fetched results.  
    
* **How it works (The File Handle Analogy):**  
 

  * A cursor behaves exactly like a file handle in programming.  
  *   
  * Just as you open a file, read its contents tracking your current line, and then close it—you open a cursor, fetch query results tracking your current row position, and then close it.  
  *   
* **Isolation Rule:** Cursors created from the same connection are **NOT** isolated. If one cursor makes a change to the database, the other cursors on that same connection can see those changes immediately.  
 

## **4\. Standard DB-API Coding Workflow (5 Steps)**

Whenever you write Python code to query a database, you will follow this exact sequence:

1. **Import:** Import the specific database module/library (e.g., import psycopg2).  
2.   
3. **Connect:** Use the connect() constructor and pass in your credentials (database name, username, password) to create a **Connection Object**.  
4.   
5. **Create Cursor:** Call the .cursor() method on your connection object to create a **Cursor Object**.  
6.   
7. **Execute & Fetch:** Use the cursor to run your SQL queries and fetch the results into your application.  
8.   
9. **Close:** Call .close() on the connection to shut it down. **Crucial Rule:** Always close unused connections to prevent them from eating up system resources\!

# **Day 12\.**

# **SQL Notes: Jupyter Notebook Magic Commands & SQL Magic**

## **1\. What are Magic Statements?**

* **Definition:** Special commands in Jupyter Notebooks that provide extra functionalities.  
    
* **Nature:** They are not valid Python code, but they change how the notebook behaves to solve common data analysis problems.  
 

## **2\. Line Magics vs. Cell Magics**

Magic commands are divided into two main categories:

| Feature | Line Magics | Cell Magics |
| :---- | :---- | :---- |
| **Prefix** | Single Percentage (%) | Double Percentage (%%) |
| **Scope** | Operates on a single line of input only. | Operates on multiple lines (the entire cell). |
| **Usage Rule** | You can use multiple line magics in one cell (each on a new line). | Must be placed at the very top of the cell. |
| **Example** | %timeit (Times one single statement) | %%timeit (Times the whole cell's execution) |

## **3\. Popular Magic Commands (Cheat Sheet)**

| Command | Type | What it does |
| :---- | :---- | :---- |
| %pwd | Line | Prints the Current Working Directory (folder path). |
| %ls | Line | Lists all files present in the current directory. |
| %history | Line | Shows the history of all executed commands. |
| %who | Line | Lists all user-defined variables in the memory. |
| %whos | Line | Gives detailed information about all variables (type, data). |
| %reset | Line | Deletes all variables and resets the namespace. |
| %matplotlib inline | Line | Forces Matplotlib plots to display directly inside the notebook. |
| %lsmagic | Line | Lists all available magic commands in Jupyter. |
| %%writefile filename.txt | Cell | Writes the entire contents of the cell into a text file. |

## **4\. Running Other Languages (Cell Magics)**

Cell magics allow you to run code other than Python inside a Jupyter cell.

* %%HTML**:** Renders HTML code (e.g., \<h1\>Hello World\</h1\>).  
   
* %%JS **or** %%Javascript**:** Runs JavaScript code (e.g., pop-up alerts).  
    
* %%bash**:** Runs terminal/command-prompt commands (e.g., echo "Hello").  
  

## **5\. SQL Magic: Accessing Databases in Jupyter**

To write direct SQL queries inside a Jupyter Notebook, follow this exact 4-step workflow:

**Step 1: Install the Dependency**

Run this in a cell to install the required library:

Python  
\!pip install ipython-sql

**Step 2: Load the SQL Extension**

Enable SQL magic in your notebook:

Python  
%load\_ext sql

**Step 3: Establish the Connection**

Connect to your specific database (Example using SQLite3 and a database named HR.db):

Python  
%sql sqlite:///HR.db

**Step 4: Run SQL Queries**

Now you can write SQL queries directly\!

* **For a short, 1-line query:**  
 

SQL  
%sql SELECT \* FROM employee LIMIT 5;

* **For a complex, multi-line query:**  
 

SQL  
%%sql  
SELECT department, COUNT(\*)   
FROM employee   
GROUP BY department;

# 

# **Day 12\.**

# **Data Analysis with Python (SQL, Pandas & Seaborn)**

**Exploratory Data Analysis (EDA)** is the process of investigating datasets to discover patterns, spot anomalies (outliers), and test hypotheses using summary statistics and graphical representations.

## **1\. Database Setup: Storing CSV Data into SQL**

Instead of analyzing raw CSV files, Data Analysts often load data into a local database for efficient querying. SQLite3 is a serverless, zero-configuration SQL database engine built into Python.

* **Step 1: Read the CSV file using Pandas.**  

Python  
import pandas as pd  
import sqlite3

data \= pd.read\_csv('mcdonalds\_menu.csv')

* **Step 2: Connect to the SQLite Database.**  
 

Python  
conn \= sqlite3.connect('mcdonalds.db')

* **Step 3: Load the Pandas DataFrame into the SQL Database.**  
 

Python  
data.to\_sql('mcdonalds\_nutrition', conn)

*(The CSV data is now officially saved as a table named* mcdonalds\_nutrition *in your SQL database).*

## **2\. Retrieving Data: SQL to Pandas**

To analyze the data, you pull it back from the SQL database into a Pandas DataFrame using a standard SQL query.

* **Method:** pd.read\_sql()  


Python  
query \= "SELECT \* FROM mcdonalds\_nutrition"  
df \= pd.read\_sql(query, conn)

\# View the first 5 rows  
df.head()

## **3\. Basic Exploratory Data Analysis (EDA)**

Pandas provides built-in statistical methods to quickly understand your dataset.

* df.describe()**:** Generates summary statistics (count, mean, standard deviation, minimum, maximum, and percentiles) for all numeric columns.  
    
* **Finding Specific Extremes (e.g., Highest Sodium Item):** If df.describe() shows the maximum sodium is 3600mg, you need to find which item that is.  
  

Python  
\# Find the index (row number) of the maximum sodium value  
max\_index \= df\['Sodium'\].idxmax()  \# Output: 82

\# Find the exact item name at that index  
item\_name \= df.at\[max\_index, 'Item'\]  \# Output: Chicken McNuggets (40 pieces)

**Conceptual Output Table (How Python sees the data):**

| Index | Category | Item | Protein | Total Fat | Sodium | Sugars |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 80 | Chicken & Fish | Chicken McNuggets (10 pcs) | 22 | 19 | 900 | 0 |
| 81 | Chicken & Fish | Chicken McNuggets (20 pcs) | 44 | 38 | 1800 | 0 |
| 82 | Chicken & Fish | Chicken McNuggets (40 pcs) | 87 | 74 | 3600 | 1 |

## **4\. Visualizing Data with Seaborn**

Visualizations help you instantly spot relationships, correlations, and outliers that numbers alone cannot show.

* swarmplot() **(Categorical Scatter Plot):**  
  

  * **Use Case:** To see the distribution of a continuous variable across different categories.  
      
  * **Example:** Plotting Category on the X-axis and Sodium on the Y-axis. It clearly visually separates the extreme 3600mg outlier from the rest of the standard menu items.  
     
* jointplot() **(Scatter Plot with Histograms):**  
 

  * **Use Case:** To check the correlation (relationship) between two numeric variables.  
      
  * **Example:** Plotting Protein vs. Total Fat. If the points form a straight upward line, it indicates a positive correlation (as protein increases, fat generally increases). It also calculates the Pearson correlation coefficient (e.g., 0.81, meaning a strong positive relationship).  
      
* boxplot()**:**  
 

  * **Use Case:** Excellent for showing data distribution and spotting outliers.  
     
  * **Structure:** The main "box" captures the middle 50% of the data. The lines (whiskers) show the standard range. Individual dots outside the lines are extreme outliers.  
     
  * **Example:** A boxplot for Sugars shows the average is around 30g, but highlights isolated dots at 128g (likely large milkshakes or McFlurries).

