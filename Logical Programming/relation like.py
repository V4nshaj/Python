import pytholog as pl
r=pl.KnowledgeBase("relation")
r(["likes(john,mary)"])
print(r.query(pl.Expr("likes(john,mary)")))
