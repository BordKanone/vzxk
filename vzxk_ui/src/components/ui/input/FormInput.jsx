import React from "react";
import classes from './FormInput.module.css'

export default function FormInput(props){
    return(
        <input className={classes.formInput} {...props} />
    )
}