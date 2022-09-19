# project3GEO


##The process 

For the project the Goal is to find the perfect location for our new offices. 
To do this we take into account the requests from our valued employees.  We decided to set our focus on the United States to narrow down our search area. 

After plotting the heat map we determined that the majority of companies are located on the south east of the states in California. After removing all the countries and states that do not match  USA and ‘CA’ and removing the rows that were still lacking long/lat data, address information for their offices. For the ease of the search we dropped all rows that were missing any of these values. After this we were left with 2401 rows of data.

To determine which requirements to take into account for the decision we researched different salary levels of the employees. We used the website glass door to get this information. For each position we took the average income and multiplied it by the total number of employees on this position to get a total spending per employee category. By doing this we ended up with the following dataframe.  The total spending category was then multiplied with the weight factor for each position, the final table creates the order of importance for the location of the office.

We decided on the weight by checking the request the group made and how big the group of employees is. 
Front-end and back-end developers fall under the same group and therefore are above the executives 

The list of requests set by the campany is:

- 30% of the company staff have at least 1 child.
- Everyone in the company is between 25 and 40, give them some place to go party.
- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Account managers need to travel a lot.
- Executives like Starbucks A LOT. Ensure there's a Starbucks not too far.
- The CEO is vegan. 
- If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.

![image](https://user-images.githubusercontent.com/104360125/182217388-ead85e5a-391d-4431-a3e7-36e4ed537195.png)


While creating the final read me we realised that we forgot to implement one of the requests because on Friday we understood we only had to look at tech companies which is all the companies in the database. The ranking of front end and back end developers was therefore ignored. The need for a place to party and having schools nearby got preference since these groups have the largest number of people in them. 

##Heat map for Los Angeles of from the MondoDB- Companies


![Screenshot 2022-08-01 at 19 01 46](https://user-images.githubusercontent.com/104360125/182218561-29f90dea-a4b9-4dcb-956e-454d0627d830.png)




To further reduce the number of possible locations for the office in LA we created a function that will keep eliminating offices that do not meet the requests made by the company. We use the following function to do this.

##Function for reducing the dataframe and making it meet all the requirements.



After applying all the filters we ended up with four possible locations. 

#All locations fall within this map  

![Screenshot 2022-08-01 at 19 03 25](https://user-images.githubusercontent.com/104360125/182219150-9d57c759-2850-4002-9a0c-f92b52297cc6.png)


All the locations are showcased in the following visualisations 



![Screenshot 2022-08-01 at 20 29 40](https://user-images.githubusercontent.com/104360125/182219248-422e99d1-1f90-417b-b3c6-9e64a7a3aafc.png)



#option 1 Social platform

![Screenshot 2022-08-01 at 20 29 47](https://user-images.githubusercontent.com/104360125/182219282-893a65be-f00a-4ce3-8709-b073c17309b0.png)


#option 2 Daily Strength

![Screenshot 2022-08-01 at 20 29 56](https://user-images.githubusercontent.com/104360125/182219302-b99fbe44-f6b0-4ac4-9a11-80b4c3725d8d.png)


#option 3 Trafficz

![Screenshot 2022-08-01 at 20 33 01](https://user-images.githubusercontent.com/104360125/182219573-02a904d7-3bd2-4cb4-81d0-c7692520e2c7.png)


#option 4 Attention span Media

![Screenshot 2022-08-01 at 20 33 01](https://user-images.githubusercontent.com/104360125/182219573-02a904d7-3bd2-4cb4-81d0-c7692520e2c7.png)



We have requested comments from a local expert with authority to make a final decision on what office we should pick in LA and he recommended us to go with.


Since we cannot make assumptions or bias influence the dicision we had a closer look at the data from the maps we have shown you before. We realised that option 3 and 4 which is why we decided to go with this location as this is the only location that had another tech companiy within rnage and this is the request we forgot and mentioned earlier.



Did you know?

Some of the top gaming companies in LA are:

- Naughty dog
- EA sports 
- Playstation 
- Riot Dog


