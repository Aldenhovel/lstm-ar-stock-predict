import React, {Fragment} from "react";
import {Card} from "antd";
import {BranchesOutlined, CalendarOutlined, GithubOutlined, UserOutlined} from "@ant-design/icons";

class InformationPage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {

        }

        this.buttonCss = {
            marginRight: '10px',
            height: '40px',
            width: '200px',
            fontFamily: "'Euclid', sans-serif",
            fontSize: '18px',
        }

        this.cardCss = {
            backgroundColor: '#F0F0F0',
            width: '95%',
            margin: '10px auto',
            fontFamily: "'Euclid', sans-serif"
        }
    }


    render() {
        return (
            <Fragment>
                <Card style={{...this.cardCss}}>
                    <p style={{fontSize: '24px', margin: '0 0 10px'}}>Version Information</p>
                    <ul style={{fontSize: '20px', margin: '0 0 10px'}}>
                        <li><BranchesOutlined/> v0.2-20240415</li>
                        <li><CalendarOutlined/> 2024-4-15</li>
                        <li><UserOutlined/> aldenhovel</li>
                        <li><GithubOutlined/>  <a href={'https://github.com/Aldenhovel/lstm-ar-stock-predict'}>https://github.com/Aldenhovel/lstm-ar-stock-predict</a></li>
                    </ul>
                </Card>

                <Card style={{...this.cardCss}}>
                    <p style={{fontSize: '24px', margin: '0 0 10px'}}>Change Log</p>
                    <ul style={{fontSize: '20px', margin: '0 0 10px'}}>
                        <li>The front-end program is now developed based on React.js, and the development of historical versions based on Vue.js will be suspended.</li>
                        <li>The project now uses echarts interactive charts to display data.</li>
                        <li>The back-end framework implementation has been rearranged to be more standardized.</li>
                    </ul>
                </Card>
            </Fragment>



        )
    }
}

export default InformationPage;