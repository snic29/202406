In a rectangular prism of size length=X width=Y, height=Z there are introduced N items (where N<=10). Each item is a solid 3 dimensional body with its distinct color C[n] <>0 for n=1,N. The item n has same color C[n]  both inside and on the surface. After all N items are introduced in the prism, the prism is filled with gas having color K=0. It is assumed that gas will fill all empty spaces of the rectangular prism. Using a digital 3D scanner we scan the prism and the scanner produces a 3 dimensions list  Z x Y x X
S=[ [ 
      [ a111, a211, .... aX11],
      [ a121, a221, .... aX21],
 ......
      [ a1Y1, a2Y1, .... aXY1],
    ],
    [ 
      [ a112, a212, .... aX12],
      [ a122, a222, .... aX22],
 ......
      [ a1Y2, a2Y2, .... aXY2],
    ],
........
.........
    [ 
      [ a11Z, a21Z, .... aX1Z],
      [ a12Z, a22Z, .... aX2Z],
 ......
      [ a1YZ, a2YZ, .... aXYZ]
    ]
]
where a[i][j][k] where i=1,Z j=1,Y k=1,X has the value of either K=0 or one of the N colors C[1],.. C[N] 
create the python code using numpy to determine for eac item n=1,N : 1) the largest distance of the item. This would be the largest distance between any two points on the surface of that item n. A surface point is any point that has a neighbougring one with a different color 2) for largest distance determined at step 1, print the full path with coordinates of each point
