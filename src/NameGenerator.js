import React, { useState, useEffect } from "react";
import axios from "axios";
import "./styles.css";

const NameGenerator = () => {
    const [randomName, setRandomName] = useState("");

    // Function to fetch a new name
    const fetchName = async () => {
        try {
            const response = await axios.get("/api/name");
            setRandomName(response.data.name);
        } catch (error) {
            console.error("Error fetching name:", error);
        }
    };

    // Fetch a name on initial load
    useEffect(() => {
        fetchName();
    }, []);

    return (
        <div className="container">
            <h1>Name That Thing</h1>
            <div className="name-display">{randomName}</div>
            <button onClick={fetchName}>Generate New Name</button>
        </div>
    );
};

export default NameGenerator;
