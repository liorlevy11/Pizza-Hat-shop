import sys
from _repository import repo
from orders import orders
from suppliers import suppliers
from hats import hats
def main():
    repo.create_tables()
    input = open(sys.argv[1])#check
    x = 0
    for line in input:
        if x == 0:
            x+=1
            continue  
        line = line.rstrip()
        args = line.split(',')
        if len(args) == 4:
            hat = hats(*args)
            repo.hats.insert(hat)
        if len(args) == 2:
            supplier = suppliers(*args)
            repo.suppilers.insert(supplier)           
   

     
    input = open(sys.argv[2])
    output = open(sys.argv[3], 'w+')
    i=1
    for line in input:
        line = line.rstrip()
        args = line.split(',')
        topping = args[1]
        thisHat=repo.hats.find(str(topping))
        hat_id = thisHat.id
        order = orders(i,args[0],hat_id)
        i = i + 1
    
        repo.orders.insert(order)

        supplier_id=thisHat.supplier
        supplier_name = repo.suppilers.find(supplier_id).name

        output.write(topping+","+supplier_name + ","+order.location +"\n")

        if thisHat.quantity > 1:
            repo.hats.update(thisHat)          
        else:
            repo.hats.delete(thisHat)
                 
    

if __name__ == '__main__':
    main()
