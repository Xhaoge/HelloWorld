from . import db

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key=True)
    cate_name = db.Column(db.String(30),nullable=False)
    topics = db.relationship('Topic',backref='category',lazy='dynamic')
    def __repr__(self):
        return "<Category:%r>"%self.cate_name

class BlogType(db.Model):
    __tablename__  = 'blogtype'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(20),nullable=False)
    topics = db.relationship('Topic',backref='blogtype',lazy='dynamic')

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    loginname = db.Column(db.String(50),nullable=False)
    uname = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    url = db.Column(db.String(200))
    upwd = db.Column(db.String(30),nullable=False)
    is_author = db.Column(db.SmallInteger,default=0)
    # 在user中,增加与topic和user之间的反向引用关系(多对多)
    vokes_topics = db.relationship('Topic',secondary='voke',lazy='dynamic',
                                   backref=db.backref('users',lazy='dynamic'))
    # 增加和topic之间的反向引用关系
    topics = db.relationship('Topic',backref='user',lazy='dynamic')
    #增加和reply之间的反向引用关系
    replies = db.relationship('Reply',backref='user',lazy='dynamic')

    def __repr__(self):
        return "<User:%r>"%self.uname

# 建立第三方数据库;
Voke= db.Table(
    'voke',
    db.Column('id',db.Integer,primary_key=True),
    db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'))
)

class Topic(db.Model):
    __tablename__ = 'topic'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    pub_date = db.Column(db.DateTime,nullable=False)
    read_num = db.Column(db.Integer,default=0)
    content = db.Column(db.TEXT,nullable=False)
    images = db.Column(db.TEXT, nullable=True)
    # 建立和blogtype的一对多的关系
    blogtype_id = db.Column(db.Integer,db.ForeignKey('blogtype.id'))
    # 建立和category的一对多的关系
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    # 建立和user的一对多的关系
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    #建立和reply的关联属性和反向引用
    replies = db.relationship('Reply',backref='topic',lazy='dynamic')

class Reply(db.Model):
    __tablename__ = 'reply'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.TEXT,nullable=False)
    reply_time = db.Column(db.DateTime,nullable=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    topic_id = db.Column(db.Integer,db.ForeignKey('topic.id'))


