import React, { useState, useEffect } from "react";
import axios from "axios";
import "./styles.css";

const NameGenerator = () => {
    const [randomName, setRandomName] = useState("");

    const fetchName = async () => {
        try {
            const response = await axios.get("/api/name");
            setRandomName(response.data.name);
        } catch (error) {
            console.error("Error fetching name:", error);
        }
    };

    useEffect(() => {
        fetchName();
    }, []);

    return (
        <div className="container">
            <div className="heading">Name that Thing</div>
            <div className="name-display">{randomName}</div>
            <button onClick={fetchName}>And another one...</button>
        </div>
    );
};

export default NameGenerator;
