import React, {Fragment} from "react";
import {Card, Button, Popconfirm} from "antd";
import {CheckOutlined, CloseOutlined} from "@ant-design/icons";

class SettingsPage extends React.Component {

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

    handleReloadUI = () => {
        window.location.reload();
    }

    render() {
        return (
            <Fragment>
                <Card style={{...this.cardCss}}>
                    <p style={{fontSize: '24px', margin: '0 0 10px'}}>Clean up</p>
                    <Button disabled type={"primary"} style={{...this.buttonCss}}>Clean test files</Button>
                    <Button disabled type={"primary"} style={{...this.buttonCss}}>Clean log files</Button>
                </Card>
                <Card style={this.cardCss}>
                    <p style={{fontSize: '24px', margin: '0 0 10px'}}>Reload</p>
                    <Popconfirm title={"Reload UI now?"} okText={<><CheckOutlined /> Yes</>} cancelText={<><CloseOutlined /> No</>} onConfirm={this.handleReloadUI} onCancel={() => {}}>
                        <Button type={"primary"} style={{...this.buttonCss}}>Reload UI</Button>
                    </Popconfirm>

                    <Button disabled type={"primary"} style={{...this.buttonCss}}>Reload Backend</Button>
                </Card>
            </Fragment>



        )
    }
}

export default SettingsPage;