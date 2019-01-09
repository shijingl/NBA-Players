from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, drop_database, create_database

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db', connect_args={'check_same_thread': False})

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
user1 = User(name="Shijing Liu", email="liushijing123@gmail.com",
             picture='https://i0.wp.com/usatodaytrending.com/wp-content/uploads/2018/12/39008hi-res-59a5e84117860a6b21563b9fc07ea45c_crop_exact.jpg?fit=1024%2C1024')
session.add(user1)
session.commit()

# Items for Strings
team1 = Category(name="Toronto Raptors", user_id=1)

session.add(team1)
session.commit()

player1 = CategoryItem(name="Kawhi Leonard", user_id=1, description="Kawhi Anthony Leonard is an American professional basketball player for the Toronto Raptors of the National Basketball Association. Selected with the 15th overall pick in the 2011 NBA draft, Leonard was named to the NBA All-Rookie First Team in his first season with the San Antonio Spurs.", category=team1)

session.add(player1)
session.commit()

player2 = CategoryItem(name="Kyle Lowry", user_id=1,  description="Kyle Lowry is an American professional basketball player for the Toronto Raptors of the National Basketball Association. He attended Cardinal Dougherty High School in Philadelphia and declared for the NBA draft after two seasons of college basketball with the Villanova Wildcats.", category=team1)

session.add(player2)
session.commit()

player3 = CategoryItem(name="Danny Green", user_id=1, description="Daniel Richard Green Jr. is an American professional basketball player for the Toronto Raptors of the National Basketball Association. He played college basketball for the University of North Carolina, where he played in more games and had more wins than any Tar Heel before him.", category=team1)

session.add(player3)
session.commit()

# Items for Woodwinds
team2 = Category(name="Golden State Warriors", user_id=1)

session.add(team2)
session.commit()

player1 = CategoryItem(name="Stephen Curry", user_id=1, description="Wardell Stephen Curry II is an American professional basketball player for the Golden State Warriors of the National Basketball Association. Many players and analysts have called him the greatest shooter in NBA history.", category=team2)

session.add(player1)
session.commit()

player2 = CategoryItem(name="Kevin Durant", user_id=1,  description="Kevin Wayne Durant is an American professional basketball player for the Golden State Warriors of the National Basketball Association. He played one season of college basketball for the University of Texas, and was selected as the second overall pick by the Seattle SuperSonics in the 2007 NBA draft.", category=team2)

session.add(player2)
session.commit()

player3 = CategoryItem(name="Draymond Green", user_id=1, description="Draymond Jamal Green Sr. is an American professional basketball player for the Golden State Warriors of the National Basketball Association. Green, who plays primarily at the power forward position, is a three-time NBA champion and a three-time NBA All-Star. In 2017, he won the NBA Defensive Player of the Year.", category=team2)

session.add(player3)
session.commit()

# Items for Percussion
team3 = Category(name="Milwaukee Bucks", user_id=1)

session.add(team3)
session.commit()

player1 = CategoryItem(name="Giannis Antetokounmpo", user_id=1, description="Giannis Antetokounmpo is a Greek professional basketball player for the Milwaukee Bucks of the National Basketball Association. Nicknamed the Greek Freak due to his athleticism, he primarily plays forward, but is also capable of playing guard with his ball-handling skills.", category=team3)

session.add(player1)
session.commit()

player2 = CategoryItem(name="Khris Middleton", user_id=1, description="James Khristian Middleton is an American professional basketball player for the Milwaukee Bucks of the National Basketball Association. He attended Porter-Gaud School, where he was coached by John Pearson.", category=team3)

session.add(player2)
session.commit()

player3 = CategoryItem(name="Brook Lopez", user_id=1, description="Brook Robert Lopez is an American professional basketball player for the Milwaukee Bucks of the National Basketball Association. He was selected 10th overall by the Nets in the 2008 NBA draft, after playing two years of college basketball for the Stanford Cardinal.", category=team3)

session.add(player3)
session.commit()

# Items for Brass
team4 = Category(name="Denver Nuggets", user_id=1)

session.add(team4)
session.commit()

player1 = CategoryItem(name="Isaiah Thomas", user_id=1, description="Isaiah Jamar Thomas is an American professional basketball player for the Denver Nuggets of the National Basketball Association. The 5-foot-9-inch point guard played three years of college basketball for the Washington Huskies and was a three-time all-conference selection in the Pac-10.", category=team4)

session.add(player1)
session.commit()

player2 = CategoryItem(name="Nikola Jokic", user_id=1, description="Nikola Jokic is a Serbian professional basketball player for the Denver Nuggets of the National Basketball Association. He also represents the Serbian national basketball team internationally. Standing at 7 ft 0 in, he plays at the center position.", category=team4)

session.add(player2)
session.commit()

player3 = CategoryItem(name="Jamal Murray", user_id=1, description="Jamal Murray is a Canadian professional basketball player for the Denver Nuggets of the National Basketball Association. He played one season of college basketball for the Kentucky Wildcats before being drafted by the Nuggets with the seventh overall pick in the 2016 NBA draft.", category=team4)

session.add(player3)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
