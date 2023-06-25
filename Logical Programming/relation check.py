import pytholog as pl
relations = pl.KnowledgeBase("relation")
relations(["male(john)", 
        "female(pinky)", # pinky is female
        "female(mary)",#mary is female
        "wife(mary,john)",#mary is wife of john
        "spouse(john,mary)",#john is spouse of mary
        "daughter(pinky,john)",#pinky is daughetr of john
        "daughter(pinky,mary)",#pinky is daughter of mary
           "male(santhanu)",# santhanu is male
#LHS and RHS in a rule are separated with “:-”.
        "wife(X):- female(X)",	# mary is wife -> Yes	
        "spouse(X):-male(X)",	#santhanu is spouse -> No
        "daughter(X):-female(X)",#Yes
        "is_daughter(X,Y):- daughter(X,Z),wife(Y,Z)"]),#pinky is daugheter of john mary is wife of john is Pinky is daughetr of Y -> Yes        
        
 
 
print(relations.query(pl.Expr("female(pinky)")))
print(relations.query(pl.Expr("male(pinky)")))
print(relations.query(pl.Expr("female(X)")))
print(relations.query(pl.Expr("male(X)")))
print(relations.query(pl.Expr("is_daughter(pinky,mary)")))
