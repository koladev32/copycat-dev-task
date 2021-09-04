import React from "react";


interface IResult {
    count: number;
    parent?: string;
    innerHTML?: string;
    className?: string;
    value?: string;
    tag?: string;
}

const Result: React.FC<IResult> = ({count, tag, parent, value, className, innerHTML, children}) => {

    const parentNode = parent;
    let node;
    if (parent) {
        if (innerHTML) {
            node = `<${parentNode}>
                        <${tag}${className ? ` class="${className}"` : ''}${value ? ` value="${value}"` : ''}>${innerHTML}</${tag}>
                    <${parentNode}/>`
        } else {
            node = `<${parentNode}>
                        <${tag}${className ? ` class="${className}"` : ''}${value ? ` value="${value}"` : ''}/>
                    <${parentNode}/>`
        }
    } else {
        node = `<${tag}${className ? ` class="${className}"` : ''}${value ? ` value="${value}"` : ''}>${innerHTML}</${tag}>`

    }

    return (
        <div className='h-1/3 w-1/5 border-gray-200 border-2 rounded'>
            <div className="bg-gray-200 overflow-auto border-b-1 border-black p-4">
                <code>
                    {node}
                </code>
            </div>
            <div className="p-4 pb-0">
                <h3 className="font-bold">Name</h3>
                <p>{tag?.toUpperCase()}</p>
            </div>
            <div className="p-4">
                <h3 className="font-bold">Occurances:</h3>
                <p>{count}</p>
            </div>
        </div>
    )
}

export default Result;