# Computation of Lifting Flow about a flatplate
Worked on numerical simulations using python to find the solutions of Laplace equation provided the conditions.



# Concept: 
The differential form of mass and momentum conservation relate the flow variables at every point in a flow field. The equations get too complicated to solve so we make approximations related to viscosity, compressibility and finally irrotationality. These approximations reduce the governing equations to a single potential equation.

To solve this we apply the concept of Numerical Solutions. We discretize the flow field and consider a finite number of points. Using this we find the solution at any arbitrary point by interpolation. We divide the flow field into a rectangular mesh and convert the differential equations into difference equations. We know the values at the boundaries and use them to find the values at the line adjacent to the boundary. 

We push the given values at the boundaries into the field interiors using the difference equations.

# Coding:
First we defined a matrix with the given number of rows and columns containing all zeroes. We did this to initialize the conditions. We then put the boundary conditions in the matrix. We defined a value epsi=0.00001 and created an empty list in which we stored the updated values of Φ. Next we defined two for loops: to specify from where the loop starts and goes. We then identified the different points in the rectangular grid and coded the corresponding equations for them. After each corresponding equation we write a code so as to compare the previous and present value of Φ, if this difference comes less than the given epsi value the iteration stops. We then updated the Φ values by coding the formula for it(taking w into the picture=0.4). 

Then we defined another matrix for storing all the Φ values and then differentiated them using the central difference equation. On differentiating we got the velocity values.

We then plotted the x component of velocity with respect to the columns and the y component with respect to the rows. We applied the same for both coarse and fine grid with a change in number of rows and columns and the corresponding points. We applied the same coding way for the specific solution too and changed the boundary conditions according to those given to us. 



