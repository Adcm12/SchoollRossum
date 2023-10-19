from main import db

class Usuario(db.Model):
    
    nickname = db.Column(db. String(15), primary_key=True)
    nome = db.Column(db. String(15), nullable = False)
    senha = db.Column(db. String(15), nullable = False)

    def __repr__(self):

        return '<NAME %r' % self.name