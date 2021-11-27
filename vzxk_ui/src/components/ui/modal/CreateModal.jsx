import React from "react";
import classes from './CreateModal.module.css'

export default function CreateModal({children, visible, setVisible}) {

    const rootClass = [classes.CreateModal]

    if (visible) {
        rootClass.push(classes.active)
    }

    return (
        <div className={rootClass.join(' ')} onClick={()=> setVisible(false)}>
            <div className={classes.CreateModalContent} onClick={(e) => e.stopPropagation()}>
                {children}
            </div>
        </div>
    )
}