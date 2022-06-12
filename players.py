from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, drop_database, create_database

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db',
                       connect_args={'check_same_thread': False})

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
             picture='https://i0.wp.com/usatodaytrending.com/\n'
                     'wp-content/uploads/2018/12/39008hi-res-\n'
                     '59a5e84117860a6b21563b9fc07ea45c_crop\n'
                     '_exact.jpg?fit=1024%2C1024')
session.add(user1)
session.commit()

# Items for Strings
team1 = Category(name="Toronto Raptors",
                 user_id=1)

session.add(team1)
session.commit()

player1 = CategoryItem(name="Kawhi Leonard",
                       user_id=1,
                       description="Kawhi Anthony Leonard is an \n"
                       "American professional basketball player for the \n"
                       "Toronto Raptors of the National Basketball \n"
                       "Association. Selected with the 15th overall \n"
                       "pick in the 2011 NBA draft, Leonard was named \n"
                       "to the NBA All-Rookie First Team in his first \n"
                       "season with the San Antonio Spurs.",
                       category=team1)

session.add(player1)
session.commit()

player2 = CategoryItem(name="Kyle Lowry",
                       user_id=1,
                       description="Kyle Lowry is an American professional \n"
                       "basketball player for the Toronto Raptors of \n"
                       "the National Basketball Association. He attended \n"
                       "Cardinal Dougherty High School in Philadelphia and \n"
                       "declared for the NBA draft after two seasons of \n"
                       "college basketball with the Villanova Wildcats.",
                       category=team1)

session.add(player2)
session.commit()

player3 = CategoryItem(name="Danny Green",
                       user_id=1,
                       description="Daniel Richard Green Jr. is an \n"
                       "American professional basketball player for \n"
                       "the Toronto Raptors of the National Basketball \n"
                       "Association. He played college basketball for the \n"
                       "University of North Carolina, where he played in \n"
                       "more games and had more wins than any Tar Heel \n"
                       "before him.",
                       category=team1)

session.add(player3)
session.commit()

# Items for Woodwinds
team2 = Category(name="Golden State Warriors",
                 user_id=1)

session.add(team2)
session.commit()

player1 = CategoryItem(name="Stephen Curry",
                       user_id=1,
                       description="Wardell Stephen Curry II is an \n"
                       "American professional basketball player for \n"
                       "the Golden State Warriors of the National \n"
                       "Basketball Association. Many players and \n"
                       "analysts have called him the greatest shooter \n"
                       "in NBA history.",
                       category=team2)

session.add(player1)
session.commit()

player2 = CategoryItem(name="Kevin Durant",
                       user_id=1,
                       description="Kevin Wayne Durant is an American \n"
                       "professional basketball player for the Golden \n"
                       "State Warriors of the National Basketball \n"
                       "Association. He played one season of college \n"
                       "basketball for the University of Texas, and \n"
                       "was selected as the second overall pick by \n"
                       "the Seattle SuperSonics in the 2007 NBA draft.",
                       category=team2)

session.add(player2)
session.commit()

player3 = CategoryItem(name="Draymond Green",
                       user_id=1,
                       description="Draymond Jamal Green Sr. is an \n"
                       "American professional basketball player for \n"
                       "the Golden State Warriors of the National \n"
                       "Basketball Association. Green, who plays \n"
                       "primarily at the power forward position, is \n"
                       "a three-time NBA champion and a three-time \n"
                       "NBA All-Star. In 2017, he won the NBA Defensive \n"
                       "Player of the Year.",
                       category=team2)

session.add(player3)
session.commit()

# Items for Percussion
team3 = Category(name="Milwaukee Bucks",
                 user_id=1)

session.add(team3)
session.commit()

player1 = CategoryItem(name="Giannis Antetokounmpo",
                       user_id=1,
                       description="Giannis Antetokounmpo is a Greek \n"
                       "professional basketball player for the \n"
                       "Milwaukee Bucks of the National Basketball \n"
                       "Association. Nicknamed the Greek Freak due \n"
                       "to his athleticism, he primarily plays forward, \n"
                       "but is also capable of playing guard with his \n"
                       "ball-handling skills.",
                       category=team3)

session.add(player1)
session.commit()

player2 = CategoryItem(name="Khris Middleton",
                       user_id=1,
                       description="James Khristian Middleton is an \n"
                       "American professional basketball player for \n"
                       "the Milwaukee Bucks of the National Basketball \n"
                       "Association. He attended Porter-Gaud School, \n"
                       "where he was coached by John Pearson.",
                       category=team3)

session.add(player2)
session.commit()

player3 = CategoryItem(name="Brook Lopez",
                       user_id=1,
                       description="Brook Robert Lopez is an American \n"
                       "professional basketball player for the \n"
                       "Milwaukee Bucks of the National Basketball \n"
                       "Association. He was selected 10th overall by \n"
                       "the Nets in the 2008 NBA draft, after playing \n"
                       "two years of college basketball for the \n"
                       "Stanford Cardinal.",
                       category=team3)

session.add(player3)
session.commit()

# Items for Brass
team4 = Category(name="Denver Nuggets",
                 user_id=1)

session.add(team4)
session.commit()

player1 = CategoryItem(name="Isaiah Thomas",
                       user_id=1,
                       description="Isaiah Jamar Thomas is an American \n"
                       "professional basketball player for the Denver \n"
                       "Nuggets of the National Basketball Association. \n"
                       "The 5-foot-9-inch point guard played three years \n"
                       "of college basketball for the Washington Huskies \n"
                       "and was a three-time all-conference selection in \n"
                       "the Pac-10.",
                       category=team4)

session.add(player1)
session.commit()

player2 = CategoryItem(name="Nikola Jokic",
                       user_id=1,
                       description="Nikola Jokic is a Serbian professional \n"
                       "basketball player for the Denver Nuggets of the \n"
                       "National Basketball Association. He also \n"
                       "represents the Serbian national basketball \n"
                       "team internationally. Standing at 7 ft 0 \n"
                       "in, he plays at the center position.",
                       category=team4)

session.add(player2)
session.commit()

player3 = CategoryItem(name="Jamal Murray",
                       user_id=1,
                       description="Jamal Murray is a Canadian \n"
                       "professional basketball player for the Denver \n"
                       "Nuggets of the National Basketball Association. \n"
                       "He played one season of college basketball for \n"
                       "the Kentucky Wildcats before being drafted by the \n"
                       "Nuggets with the seventh overall pick in the \n"
                       "2016 NBA draft.",
                       category=team4)

session.add(player3)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print("Category: " + category.name)
