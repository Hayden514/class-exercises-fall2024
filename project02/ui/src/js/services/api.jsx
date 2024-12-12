const rootURL = "http://localhost:8000";

// React Task 1:
export async function fetchUser(username) {
    const response = await fetch(`${rootURL}/api/users/${username}`);
    if (!response.ok) {
        throw new Error("Failed to fetch user");
    }
    const user = await response.json();
    return user;
}

// React Task 2:
export async function fetchDepartments() {
    const response = await fetch(`${rootURL}/api/departments`);
    if (!response.ok) {
        throw new Error("Failed to fetch departments");
    }
    const departments = await response.json();
    return departments;
}

// React Task 3:
export async function fetchCourses(options = {}) {
    let baseURL = `${rootURL}/api/courses?`;
    if (options.department) {
        baseURL += `department=${options.department}&`;
    }
    if (options.instructor) {
        baseURL += `instructor=${options.instructor}&`;
    }
    if (options.hours) {
        baseURL += `hours=${options.hours}&`;
    }
    if (options.title) {
        baseURL += `title=${options.title}&`;
    }
    if (options.classifications) {
        baseURL += `classifications=${options.classifications.join(",")}&`;
    }
    if (options.days) {
        baseURL += `days=${options.days.join(",")}&`;
    }
    if (options.open) {
        baseURL += `open=${options.open}&`;
    }
    console.log(baseURL);
    const response = await fetch(baseURL);
    if (!response.ok) {
        throw new Error("Failed to fetch courses");
    }
    const courses = await response.json();
    console.log(courses);
    return courses;
}

export async function fetchSchedule(username) {
    const response = await fetch(`${rootURL}/api/schedules/${username}`);
    return await response.json();
}

export async function deleteCourseFromSchedule(schedule, crn) {
    const url = `${rootURL}/api/schedules/${schedule.id}/courses/${crn}`;
    const response = await fetch(url, {
        method: "DELETE",
    });
    const data = await response.json();
    console.log(data);
    return data;
}

export async function addCourseToSchedule(schedule, crn) {
    console.log(crn);
    const url = `${rootURL}/api/schedules/${schedule.id}/courses`;

    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            crn: crn,
        }),
    });
    const data = await response.json();
    console.log(data);
    return data;
}
