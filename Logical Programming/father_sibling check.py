import pytholog as pl
relations = pl.KnowledgeBase("relation")
relations(["male(john)", 
           "female(pinky)",
           "male(roger)",
           "brother(john,pinky)",
           "sister(pinky,john)",
           "father(roger,pinky)",
           "father(roger,john)",
           "is_sybiling(john,pinky):-brother(john,pinky),sister(pinky,john)",
           "is_parent(roger,pinky):-father(roger,pinky)"])
           
        
        
print(relations.query(pl.Expr("sister(john,pinky)")))
print(relations.query(pl.Expr("is_sybiling(john,pinky)")))
