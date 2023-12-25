import React, { useState } from "react";

const Query = () => {
    const [query, setQuery] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post("http://localhost:5000/query", {query})
            .then(response => {
                console.log(response.data)
            })
            .catch(error => {
                console.error("error fethcing data", error)
            })
    }

    const handleChange = (e) => {
        setQuery(e.target.value);
    }
    return (
        <div> 
            <form onSubmit={handleSubmit}>
            <div className="flex flex-row justify-center items-center">
                <textarea onChange={handleChange} id="query" name="query" rows="8" cols="50" className="block mt-5 p-2.5 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"></textarea>
            </div>
            <div className="flex flex-row justify-center items-center">
                <button type="submit" className="ml-72 align-center mt-5 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg">Submit</button>    
            </div>
            <div className="mr-72 flex flex-row justify-center items-center">
                <h1 className="text-2xl">Results:</h1>
            </div>
            </form>
        </div>
    )
}

export default Query;