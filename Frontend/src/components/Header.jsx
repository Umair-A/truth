import React from "react";
import logo from "../logo.png";

const Header = ()=>{
    return(
        <div>
            <a href="#">
                <img src={logo} alt="Logo" className="h-32 w-32"></img>
            </a>
        </div>
    )
}

export default Header;