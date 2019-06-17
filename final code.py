print "1.Baseline solution with coarse grid"
print "2.Baseline solution with fine grid"
print "3.Specific solution of team 2 with coarse grid" 
print "4.Specific solution of team 2 with fine grid"
Q = input("Enter your choice")
if Q == 1:
    import numpy 
    a = numpy.zeros((11,26))
    for b in range(1,10):
        a[b][0] = 4.0*((10-b)*0.04)*(((10-b)*0.04)-0.4)
    for k in range (1,25):
        a[0][k] = 0
    for m in range (1,25):
        a[10][m]= 0 
        
    h = 0.04
    w = 0.4
    epsi = 0.00001
    iter = 0
    while 1:
        dif_list = []
        iter +=1
        for j in range (1,10):
            for i in range (1,25):
                if j==9 and i==1:
                    at = a[j][i]      
                    a[j][i]= (a[j][i+1]+a[j-1][i]-a[j][i-1]*h-a[j+1][i]*h)/2.0
                    dif_list.append(abs(at-a[j][i]))
                   
                elif j==1 and i==1:
                    at = a[j][i]
                    a[j][i] = (a[j][i+1]+a[j+1][i]-a[j][i-1]*h+a[j-1][i]*h)/2.0
                    dif_list.append(abs(at-a[j][i]))
                    
                elif j!=9 and j!=1 and i==1:
                    at = a[j][i]
                    a[j][i]= (a[j][i+1]-a[j][i-1]*h+a[j+1][i]+a[j-1][i])/3.0
                    dif_list.append(abs(at-a[j][i]))
                                    
                elif j==1 and i!=1 and i!=24:
                    at = a[j][i]
                    a[j][i]= (a[j][i-1]+a[j][i+1]+a[j+1][i]-a[j-1][i]*h)/3.0
                    dif_list.append(abs(at-a[j][i]))
                                    
                elif j==9 and i!=1 and i!=24:
                    at = a[j][i]
                    a[j][i]= (a[j][i-1]+a[j][i+1]+a[j-1][i]-a[j+1][i]*h)/3.0
                    dif_list.append(abs(at-a[j][i]))
                else:
                    at = a[j][i]
                    a[j][i] = (a[j][i+1]+a[j][i-1]+a[j-1][i]+a[j+1][i])/4.0
                    dif_list.append(abs(at-a[j][i]))

        for j in range (1,10):
            for i in range (1,25):
                a[j][i]= a[j][i]*w+(1-w)*a[j][i]
                
        if max(dif_list) < epsi:
            break


    

    z=numpy.zeros((11,26))
    for j in range(0,11):
        for i in range(0,25):
            if j==0 or i==0 or j==10 :
                z[j][i]=a[j][i]*h
            else :
                 z[j][i]= a[j][i]
                 
                 
    c=numpy.zeros((11,26))            
    for j in range(0,10):
        for i in range(0,25):
            if j==0 or i==0 or j==10 :   
                c[j][i]=z[j][i]/h
            else:
                c[j][i]=(z[j][i+1]-z[j][i-1])/(2.0*h)
                
    
    print "Number of iterations", iter             
            
            
    import xlwt

    book = xlwt.Workbook()
    sh = book.add_sheet("sheet")
    for j in range(11):
        for i in range(26):
           sh.write(j,i,c[j][i])
    sh = book.add_sheet("sheet1")
    for j in range(11):
        for i in range(26):
           sh.write(i,j,c[j][i])
    book.save("Baselinesolution_coase_grid.xls")

    
elif Q == 2 :
    import numpy 
    a = numpy.zeros((21,51))
    for b in range(1,20):
        a[b][0] = 4.0*((20-b)*0.02)*(((20-b)*0.02)-0.4)
    for k in range (1,50):
        a[0][k] = 0
    for m in range (1,50):
        a[10][m]= 0 
        
    h = 0.02
    w = 0.4
    epsi = 0.00001
    iter = 0
    while 1:
        dif_list = []
        iter +=1
        for j in range (1,20):
            for i in range (1,50):
                if j==19 and i==1:
                    at = a[j][i]      
                    a[j][i]= (a[j][i+1]+a[j-1][i]-a[j][i-1]*h-a[j+1][i]*h)/2.0
                    dif_list.append(abs(at-a[j][i]))
                   
                elif j==1 and i==1:
                    at = a[j][i]
                    a[j][i] = (a[j][i+1]+a[j+1][i]-a[j][i-1]*h+a[j-1][i]*h)/2.0
                    dif_list.append(abs(at-a[j][i]))
                    
                elif j!=19 and j!=1 and i==1:
                    at = a[j][i]
                    a[j][i]= (a[j][i+1]-a[j][i-1]*h+a[j+1][i]+a[j-1][i])/3.0
                    dif_list.append(abs(at-a[j][i]))
                                    
                elif j==1 and i!=1 and i!=49:
                    at = a[j][i]
                    a[j][i]= (a[j][i-1]+a[j][i+1]+a[j+1][i]-a[j-1][i]*h)/3.0
                    dif_list.append(abs(at-a[j][i]))
                                    
                elif j==19 and i!=1 and i!=49:
                    at = a[j][i]
                    a[j][i]= (a[j][i-1]+a[j][i+1]+a[j-1][i]-a[j+1][i]*h)/3.0
                    dif_list.append(abs(at-a[j][i]))
                else:
                    at = a[j][i]
                    a[j][i] = (a[j][i+1]+a[j][i-1]+a[j-1][i]+a[j+1][i])/4.0
                    dif_list.append(abs(at-a[j][i]))

        for j in range (1,20):
            for i in range (1,50):
                a[j][i]= a[j][i]*w+(1-w)*a[j][i]
                
        if max(dif_list) < epsi:
            break

    z=numpy.zeros((21,51))
    for j in range(0,21):
        for i in range(0,51):
            if j==0 or i==0 or j==20 :
                z[j][i]=a[j][i]*h
            else :
                 z[j][i]= a[j][i]            
                 
    c=numpy.zeros((21,51))            
    for j in range(0,20):
        for i in range(0,50):
            if j==0 or i==0 or j==20 :   
                c[j][i]=z[j][i]/h
            else:
                c[j][i]=(z[j][i+1]-z[j][i-1])/(2.0*h)
             
    
    print "Number of iterations", iter             
            
            
    import xlwt

    book = xlwt.Workbook()
    sh = book.add_sheet("sheet")
    for j in range(21):
        for i in range(51):
           sh.write(j,i,c[j][i])
    sh = book.add_sheet("sheet1")
    for j in range(21):
        for i in range(51):
           sh.write(i,j,c[j][i])
    book.save("Baselinesolution_Fine_grid.xls")
        
elif Q == 3:
    import numpy 
    a = numpy.zeros((11,26))
    for b in range(1,10):
      a[b][0] = 4.0*((10-b)*0.04)*(((10-b)*0.04)-0.4)
    for k in range (1,25):
      a[0][k] = 0
    for m in range (1,10):
      a[m][25]= 8.0*((10-b)*0.04)*(((10-b)*0.04)-0.4)
    
    h = 0.04
    w = 0.4
    epsi = 0.00001
    while 1:
        dif_list = []
        iter +=1
        for j in range (1,10):
            for i in range (1,25):
				if j==1 and i==1:
					at = a[j][i]
					a[j][i] = (a[j][i+1]+a[j+1][i]-a[j][i-1]*h+a[j-1][i]*h)/2.0
					dif_list.append(abs(at-a[j][i]))
				elif j==1 and i==24:
					at = a[j][i]
					a[j][i]= (a[j][i-1]+a[j+1][i]+a[j-1][i]*h+a[j][i+1]*h)/2.0
					dif_list.append(abs(at-a[j][i]))
				elif j==1 and i!=1 and i!=24:
					at = a[j][i]
					a[j][i]= (a[j][i-1]+a[j][i+1]+a[j+1][i]+a[j-1][i]*h)/3.0
					dif_list.append(abs(at-a[j][i]))
				elif j!=1 and j!=9 and i==1:
					at = a[j][i]
					a[j][i]= (a[j][i+1]-a[j][i-1]*h+a[j+1][i]+a[j-1][i])/3.0
					dif_list.append(abs(at-a[j][i]))
				elif j!=1 and j!=9 and i==24:
					at = a[j][i]
					a[j][i]= (a[j][i-1]+a[j-1][i]+a[j][j+1]+a[j][i+1]*h)/3.0
					dif_list.append(abs(at-a[j][i]))
				else:
					at = a[j][i]
					a[j][i] = (a[j][i+1]+a[j][i-1]+a[j-1][i]+a[j+1][i])/4.0
					dif_list.append(abs(at-a[j][i]))

        for j in range (1,10):
            for i in range (1,25):
                a[j][i]= a[j][i]*w+(1-w)*a[j][i]
    
        if max(dif_list) < epsi:
           break

    z=numpy.zeros((11,26))
    for j in range(0,10):
      for i in range(0,26):
        if j==0 or i==0 or i==25 :
            z[j][i]=a[j][i]*h
        else :
             z[j][i]= a[j][i]            
             
    c=numpy.zeros((11,26))            
    for j in range(0,10):
      for i in range(0,26):
        if j==0 or i==0 or i==25 :   
            c[j][i]=z[j][i]/h
        else:
            c[j][i]=(z[j][i+1]-z[j][i-1])/(2.0*h)
            
        
    print "Number of iterations", iter                 
    import xlwt

    book = xlwt.Workbook()
    sh = book.add_sheet("sheet" )
    for j in range(11):
       for i in range(26):
        sh.write(j,i,c[j][i])
    sh = book.add_sheet("sheet1")
    for j in range(11):
        for i in range(26):
           sh.write(i,j,c[j][i])
    book.save("specific_coarse_grid.xls")

elif Q == 4:
    import numpy 
    a = numpy.zeros((21,51))
    for b in range(1,20):
      a[b][0] = 4.0*((20-b)*0.02)*(((20-b)*0.02)-0.4)
    for k in range (1,50):
      a[0][k] = 0
    for m in range (1,20):
      a[m][50]= 8.0*((20-b)*0.02)*(((20-b)*0.02)-0.4)
    
    h = 0.02
    w = 0.4
    epsi = 0.00001
    while 1:
        dif_list = []
        iter +=1
        for j in range (1,20):
            for i in range (1,50):
				if j==1 and i==1:
					at = a[j][i]
					a[j][i] = (a[j][i+1]+a[j+1][i]-a[j][i-1]*h+a[j-1][i]*h)/2.0
					dif_list.append(abs(at-a[j][i]))
				elif j==1 and i==49:
					at = a[j][i]
					a[j][i]= (a[j][i-1]+a[j+1][i]+a[j-1][i]*h+a[j][i+1]*h)/2.0
					dif_list.append(abs(at-a[j][i]))
				elif j==1 and i!=1 and i!=49:
					at = a[j][i]
					a[j][i]= (a[j][i-1]+a[j][i+1]+a[j+1][i]+a[j-1][i]*h)/3.0
					dif_list.append(abs(at-a[j][i]))
				elif j!=1 and j!=19 and i==1:
					at = a[j][i]
					a[j][i]= (a[j][i+1]-a[j][i-1]*h+a[j+1][i]+a[j-1][i])/3.0
					dif_list.append(abs(at-a[j][i]))
				elif j!=1 and j!=19 and i==49:
					at = a[j][i]
					a[j][i]= (a[j][i-1]+a[j-1][i]+a[j][j+1]+a[j][i+1]*h)/3.0
					dif_list.append(abs(at-a[j][i]))
				else:
					at = a[j][i]
					a[j][i] = (a[j][i+1]+a[j][i-1]+a[j-1][i]+a[j+1][i])/4.0
					dif_list.append(abs(at-a[j][i]))

        for j in range (1,20):
            for i in range (1,50):
                a[j][i]= a[j][i]*w+(1-w)*a[j][i]
    
        if max(dif_list) < epsi:
           break



    z=numpy.zeros((21,51))
    for j in range(0,21):
      for i in range(0,51):
        if j==0 or i==0 or i==50 :
            z[j][i]=a[j][i]*h
        else :
             z[j][i]= a[j][i]
             
    c=numpy.zeros((21,51))            
    for j in range(0,21):
     for i in range(0,51):
        if j==0 or i==0 or i==50 :   
            c[j][i]=z[j][i]/h
        else:
            c[j][i]=(z[j][i+1]-z[j][i-1])/(2.0*h)
            
   
    print "Number of iterations", iter                 
    import xlwt

    book = xlwt.Workbook()
    sh = book.add_sheet("sheet" )
    for j in range(21):
       for i in range(51):
        sh.write(j,i,c[j][i])
    sh = book.add_sheet("sheet1")
    for j in range(21):
        for i in range(51):
           sh.write(i,j,c[j][i])
    book.save("specific_fine_grid.xls")    