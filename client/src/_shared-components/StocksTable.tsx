import React from 'react';

const keys = ['SC_CODE', 'SC_NAME', 'OPEN', 'HIGH', 'LOW', 'CLOSE']

interface Props {
    stocks: any[];
}

const StocksTable: React.FunctionComponent<Props> = (props: Props) => {

    // table header jsx
    const header = keys.map((key, index) => {
        return (<th scope="col" key={index}>{key}</th>)
    });

    // rows jsx
    const stocks = props.stocks && props.stocks.map((stock, index) => {
        const rows = keys.map((key, index) => {
            return (
                <td key={index}>{stock[key]}</td>
            )
        });
        return (
            <tr key={index}>
                {rows}
            </tr>
        )
    });

    return (
        <div className="table-responsive-sm">  
            <table className="table table-striped text-capitalize">
                <thead className="thead-dark ">
                    <tr>
                        {header}
                    </tr>
                </thead>
                <tbody>
                    {stocks}
                </tbody>
            </table>
        </div>
    );
}

export default StocksTable;
