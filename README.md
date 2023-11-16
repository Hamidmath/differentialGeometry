# differentialGeometry
Python methods for calculating Curvature, Torsion, Angles and some features of 3d curves

When drawing a curve in a computer program, it's important to discretize it because computers can't draw an infinite number of points and lines. Dividing the curve into smaller segments and using straight lines enables us to draw the curve in any computer program. For example, while it's impossible to draw a perfect circle, we can draw a polygon with many sides to create a similar shape. Additionally, increasing the number of segments improves the precision of the curve's representation.

However, without a mathematical function, it's not possible to find the derivative or calculate the differential geometric properties of the curve (such as curvature or torsion). To address this, I provided a Python code that calculates these properties using only the "math" library, without relying on any external libraries.
