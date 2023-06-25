import pytholog as pl
r=pl.KnowledgeBase("relation")
r(["parent(subaja,oviya)",
   "mother(subaja,oviya)",
   "is_parent(X,Y):- mother(X,Y)"
      
    ])
print(r.query(pl.Expr("parent(subaja,oviya)")))
print(r.query(pl.Expr("mother(subaja,oviya)")))
print(r.query(pl.Expr("mother(X,Y)")))
