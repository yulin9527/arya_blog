# 布局类型

## card

一个带有投影的容器

**示例**

```python
from nicegui import ui

# 基本使用
with ui.card():
    ui.label('这是一个card')

# 删除阴影 设置边框宽度
with ui.card().classes('no-shadow border-[1px]'):
    ui.label('删除了阴影')

columns = [{'name': 'age', 'label': 'Age', 'field': 'age'}]
rows = [{'age': '16'}, {'age': '18'}, {'age': '21'}]

# 嵌套使用
with ui.row():
    with ui.card():
        ui.table(columns, rows).props('flat bordered')
    # 删除 card 的边距
    with ui.card().tight():
        ui.table(columns, rows).props('flat bordered')
    with ui.card():
        with ui.row():
            ui.table(columns, rows).props('flat bordered')

ui.run()
```

### __methods

#### tight

`tight() -> Self`

删除嵌套元素之间的填充和空白。

---

## column

提供一个容器，该容器将其子容器排列在列中。

wrap:是否换行(默认:False)

**示例**

```python
from nicegui import ui

# 基本使用
with ui.column():
    ui.label('label 1')
    ui.label('label 2')
    ui.label('label 3')

# 要创建砌体/Pinterest 布局，不能使用普通布局。 但是它可以通过一些 TailwindCSS 类来实现
with ui.element('div').classes('columns-3 w-full gap-2'):
    for i, height in enumerate([50, 50, 50, 150, 100, 50]):
        tailwind = f'mb-2 p-2 h-[{height}px] bg-blue-100 break-inside-avoid'
        with ui.card().classes(tailwind):
            ui.label(f'Card #{i + 1}')

ui.run()
```

---

## row

提供一个容器，该容器将其子项排列成一行。

wrap:是否换行(默认:True)

**示例**

```python
from nicegui import ui

# 基本使用
with ui.row():
    ui.label('label 1')
    ui.label('label 2')
    ui.label('label 3')

ui.run()
```

---

## grid

提供一个容器，该容器将其子容器排列在网格中。

rows: 网格中的行数

columns: 网格中的列数

**示例**

```python
from nicegui import ui

# 基本使用
with ui.grid(columns=2):
    ui.label('Name:')
    ui.label('Tom')

    ui.label('Age:')
    ui.label('42')

    ui.label('Height:')
    ui.label('1.80m')

ui.run()
```

---

## expansion

提供一个基于类星体的QExpansionItem组件的可扩展容器。

就是折叠

text: 标题信息
icon: 要显示的图标,可选,默认None
value: 是否应该在创建时打开扩展(默认:False)
on_value_change: 当值改变时执行的回调

**示例**

```python
from nicegui import ui

with ui.expansion('Expand!', icon='work').classes('w-full'):
    ui.label('inside the expansion')

ui.run()
```

### __methods

#### close

`close() -> None`

关闭这个扩展

#### disable

`disable() -> None`

禁用这个扩展

#### enable

`enable() -> None`

激活这个扩展

#### open
`open() -> None`

打开这个扩展

#### set_enabled
`set_enabled(value: bool) -> None`

设置元素的启用状态。

#### set_value
`set_value(value: Any) -> None`

* value:  设置扩展的值


# 通用属性方法

##

## methods

### add_slot()

`add_slot(name: str, template: Optional[str] = None) -> Slot`

向该元素添加一个插槽

* name: 插槽的名称
* template: 这个插槽的 vue 模板
* return: 返回这个插槽

### bind_visibility

`bind_visibility(target_object: Any, target_name: str = 'visible', forward: Callable[..., Any] = [...], backward: Callable[..., Any] = [...], value: Any = None) -> Self`

将此元素的可见性绑定到目标对象的target_name属性。绑定是双向的，从这个元素到目标，从目标到这个元素。target_object:

### bind_visibility_from

`bind_visibility_from(target_object: Any, target_name: str = 'visible', backward: Callable[..., Any] = [...], value: Any = None) -> Self`

将此元素的可见性与目标对象的target_name属性绑定。绑定只以一种方式工作，即从目标到此元素。

### bind_visibility_to

`bind_visibility_to(target_object: Any, target_name: str = 'visible', forward: Callable[..., Any] = [...]) -> Self`

将此元素的可见性绑定到目标对象的target_name属性。绑定只以一种方式工作，即从该元素到目标。

### classes

`classes(add: Optional[str] = None, remove: Optional[str] = None, replace: Optional[str] = None) -> Self`

**应用、删除或替换HTML类。这允许使用Tailwind或Quasar类修改元素的外观或布局。如果不需要预定义的类，删除或替换类会很有帮助。**

* add: 以空格分隔的类字符串
* remove: 要从元素中删除的类的以空格分隔的字符串
* replace: 用空格分隔的类字符串来代替现有的类

### clear

`clear() -> None`
清空所有元素

### delete

`delete() -> None`
删除一个元素

### move

`move(target_container: Optional[Element] = None, target_index: int = -1)`

将元素移动到另一个容器中。

* target_container:将元素移动到的容器(默认:父容器)
* target_index:目标槽内的索引(默认:附加到末尾)

### on

`on(type: str, handler: Optional[Callable[..., Any]] = None, args: Union[None, Sequence[str], Sequence[Optional[Sequence[str]]]] = None, throttle: float = 0.0, leading_events: bool = True, trailing_events: bool = True) -> Self`

事件订阅

* type: 事件的名称(例如:“点击”、“按下鼠标”或“update:model-value”)
* handler: 事件发生时调用的回调函数
* args: 发送给事件处理程序的事件消息中包含的参数(默认值:None，即all)
* throttle: 事件发生之间的最小时间(以秒为单位)(默认:0.0)
* leading_events: 是否在第一个事件发生时立即触发事件处理程序(默认:True)
* trailing_events: 是否在最后一次事件发生后触发事件处理程序(默认:True)

### props

`props(add: Optional[str] = None, remove: Optional[str] = None) -> Self`

添加或删除道具。这允许使用类星体道具修改元素的外观或布局。由于props只是作为HTML属性应用，因此它们可以与任何HTML元素一起使用。如果没有指定值，则假定布尔属性为True。

* add: 要添加的布尔值或键=值对的以空格分隔的列表
* remove: 要删除的属性键的以空格分隔的列表

### remove

`remove(element: Union[Element, int]) -> None`

删除一个子元素

* element: 元素实例或其ID

### run_method

`run_method(name: str, *args: Any, timeout: float = 1, check_interval: float = 0.01) -> AwaitableResponse`

在客户端运行一个方法。如果等待函数，则返回方法调用的结果。否则，该方法将在不等待响应的情况下执行。

* name: 方法的名称
* args: 传递给方法的参数
* timeout: 等待响应的最大时间(默认:1秒)
* check_interval: 检查响应之间的时间间隔(默认:0.01秒)

### set_visibility

`set_visibility(visible: bool) -> None`

设置该元素的可见性

### style

`style(add: Optional[str] = None, remove: Optional[str] = None, replace: Optional[str] = None) -> Self`

应用、删除或替换CSS定义。如果不需要预定义的样式，删除或替换样式可能会有所帮助。

* add: 要添加到元素的样式列表，以分号分隔
* remove: 要从元素中删除的样式列表，以分号分隔
* replace: 要使用的样式列表，以分号分隔，而不是现有的样式

### tooltip

`tooltip(text: str) -> Self`

向元素添加工具提示

* text: 工具提示的文本信息

### update

`update() -> None`

在客户端更新元素。

---

# demo

## 清除控件内容

可以调用 clear 从 row,column 和 ard 中清除内容

container.clear()

或者,也可以通过调用
`container.remove(element:Element),container.remove(index:int),element.delete()`

```python
from nicegui import ui

container = ui.row()


def add_face():
    with container:
        ui.icon('face')


add_face()

ui.button('Add', on_click=add_face)
ui.button('Remove', on_click=lambda: container.remove(0) if list(container) else None)
ui.button('Clear', on_click=container.clear)

ui.run()
```