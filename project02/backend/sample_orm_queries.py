import asyncio
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from db import AsyncSessionLocal
from models import Course, User
from db import get_db

# Print all usernames
async def print_usernames(db: AsyncSessionLocal):
    query = select(User.username)
    result = await db.execute(query)
    usernames = result.scalars().all()
    for username in usernames:
        print(username)


# Print unique departments
async def print_unique_departments(db: AsyncSessionLocal):
    query = select(Course.department).distinct()
    result = await db.execute(query)
    departments = result.scalars().all()
    for department in departments:
        print(department)


# Print open CSCI courses
async def print_open_cs_courses(db: AsyncSessionLocal):
    query = select(Course.crn, Course.title).where(
        (Course.department == "CSCI") &
        (Course.enrollment_current < Course.enrollment_max)
    )
    
    result = await db.execute(query)
    courses = result.fetchall()
    for crn, title in courses:
        print(f"CRN: {crn}, Title: {title}")


async def main():
    # Create DB session
    db = AsyncSessionLocal()

    # Call the functions
    await print_usernames(db)
    await print_unique_departments(db)
    await print_open_cs_courses(db)

    await db.close()


if __name__ == "__main__":
    asyncio.run(main())

# Task 1: Print all usernames from the system
async def print_usernames(db: AsyncSession):
    # Query the User model to get all usernames
    result = await db.execute(select(User.username))  # username
    usernames = result.scalars().all()
    
    # Print all usernames
    print("All usernames:")
    for username in usernames:
        print(username)

# Task 2: Print unique departments from the courses
async def print_unique_departments(db: AsyncSession):
    # Query distinct departments from Course table
    result = await db.execute(select(Course.department).distinct())
    departments = result.scalars().all()
    
    # Print each unique department
    print("Unique Departments:")
    for department in departments:
        print(department)

# Task 3: Print all open CSCI courses that are not yet full
async def print_open_cs_courses(db: AsyncSession):
    # Query courses in the CSCI department that are open (enrollment is not at max)
    query = select(Course.crn, Course.title).where(
        Course.department == "CSCI",
        Course.enrollment_current < Course.enrollment_max
    )
    result = await db.execute(query)
    
    # Fetch all results
    open_courses = result.all()
    
    # Print the courses
    print("Open CSCI courses that are not full:")
    for crn, title in open_courses:
        print(f"CRN: {crn}, Title: {title}")

async def main():
    async with get_db() as db:
        await print_usernames(db)
        await print_unique_departments(db)
        await print_open_cs_courses(db)

# Run the main function
asyncio.run(main())


# ###################
# # SELECT PRACTICE #
# ###################
# # https://docs.sqlalchemy.org/en/14/orm/tutorial.html#querying

# # Query all of the users:
# query = select(User).order_by(User.id)
# # users = session.execute(query)
# users = session.scalars(query)

# # Output all of the users using regular Python:
# print(query)  # prints the SQL
# for user in users:
#     print(user.username)

# # Query all of the tasks:
# query = select(Task).order_by(Task.id)
# print(query)
# tasks = session.scalars(query)

# # Print them:
# for task in tasks:
#     print(task.name, task.user.username)

# # Query all of the tasks owned by Keith Taylor:
# query = (
#     select(Task).join(User).filter(User.username == "keith_taylor").order_by(Task.id)
# )
# print(query)
# tasks = session.scalars(query)

# for task in tasks:
#     print(task.name, task.user.username)

# # Query all of the tasks owned by Keith Taylor or Misty Baker:
# query = (
#     select(Task)
#     .join(User)
#     .filter(or_(User.username == "keith_taylor", User.username == "misty_baker"))
#     .order_by(Task.id)
# )
# print(query)
# tasks = session.scalars(query)
# for task in tasks:
#     print(task.name, task.user.username)

# ###################
# # INSERT PRACTICE #
# ###################

# # create a user:
# user = User(
#     username="walter_jones",
#     first_name="Walter",
#     last_name="Jones",
#     email="walter_jones@gmail.com",
# )

# # save it:
# session.add(user)
# session.commit()

# # verify that it worked:
# query = select(User).order_by(User.id)
# users = session.scalars(query)
# for user in users:
#     print(user.to_dict())


# # create a task:
# task = Task(name="Gym", description="Lift weights", done=False, user=user)

# # save it:
# session.add(task)
# session.commit()

# # verify that it worked:
# query = select(Task).order_by(Task.id)
# tasks = session.scalars(query)
# for task in tasks:
#     print(task.to_dict())


# ###################
# # UPDATE PRACTICE #
# ###################

# # get task #5 from the database:
# query = select(Task).where(Task.id == 5)
# result = session.execute(query).fetchone()
# print(result)  # returns as a tuple, so get the first task from the tuple
# task = None
# if result is not None:
#     task = result[0]
#     print(task.to_dict())  # before
#     task.done = True
#     session.commit()
#     print(task.to_dict())  # after


# ###################
# # DELETE PRACTICE #
# ###################

# # delete task #5
# if task is not None:
#     session.delete(task)
#     session.commit()
