import React from "react";
import eventBus from "./eventBus";

import { Menu} from 'antd';
import MenuItem from "antd/lib/menu/MenuItem";
import {FundOutlined, ReadOutlined, SettingOutlined, SlidersOutlined} from "@ant-design/icons";
const SubMenu = Menu.SubMenu;


class Nav extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        }

        this.items = {

        }

        this.itemCss = {
            fontSize:18,
            fontFamily: "'Euclid', sans-serif",
        }
    }

    handleClick = (e) => {
        console.log('click ', e);

    }

    handleSwitchPage = (e) => {
        eventBus.emit('switch-page', {to: e.key});
        //eventBus.emit('clear-state', {});
    }


    render() {
        return (
            <Menu
                style={{
                    width: '100wh',
                    height: '100vh',
                    fontSize: '18px',
                    //fontFamily: "'Euclid', sans-serif"
                }}
                defaultOpenKeys={['inference']}
                defaultSelectedKeys={['greedySearch']}
                mode="inline"
            >
                <SubMenu key={"inference"} style={this.itemCss} title={<span><FundOutlined></FundOutlined><span>Inference</span></span>}>
                    <MenuItem key="greedySearch" onClick={this.handleSwitchPage} style={this.itemCss}>
                        <SlidersOutlined></SlidersOutlined>
                        <span>Greedy Search</span>
                    </MenuItem>
                    <Menu.Item key="beamSearch" onClick={this.handleSwitchPage} style={this.itemCss}>
                        <SlidersOutlined></SlidersOutlined>
                        <span>Beam Search</span>
                    </Menu.Item>
                </SubMenu>

                <MenuItem key="settings" onClick={this.handleSwitchPage} style={this.itemCss}>
                    <SettingOutlined></SettingOutlined>
                    <span>Settings</span>
                </MenuItem>
                <MenuItem key="information" onClick={this.handleSwitchPage} style={this.itemCss}>
                    <ReadOutlined></ReadOutlined>
                    <span>Information</span>
                </MenuItem>
            </Menu>
        )
    }


}

export default Nav;