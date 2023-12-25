import React from "react";
import Header from "./Header";
import Query from "./Query";

const Index = ()=>{
    return (
        <div>
            <div className="bg-gray-800">
                <Header />
            </div>
            <div>
                <Query />
            </div>
        </div>
    )
}

export default Index;