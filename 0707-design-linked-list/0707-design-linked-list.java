class MyLinkedList {

    class Node {
        int val;
        Node next;
        Node prev;

        Node(int val) {
            this.val = val;
        }
    }

    Node head;
    Node tail;
    int size;

    public MyLinkedList() {
        size = 0;
    }

    public int get(int index) {
        if (index < 0 || index >= size)
            return -1;

        Node temp = head;

        for (int i = 0; i < index; i++) {
            temp = temp.next;
        }

        return temp.val;
    }

    public void addAtHead(int val) {
        Node newNode = new Node(val);

        if (head == null) {
            head = tail = newNode;
        } else {
            newNode.next = head;
            head.prev = newNode;
            head = newNode;
        }

        size++;
    }

    public void addAtTail(int val) {
        Node newNode = new Node(val);

        if (tail == null) {
            head = tail = newNode;
        } else {
            newNode.prev = tail;
            tail.next = newNode;
            tail = newNode;
        }

        size++;
    }

    public void addAtIndex(int index, int val) {
        if (index < 0 || index > size)
            return;

        if (index == 0) {
            addAtHead(val);
            return;
        }

        if (index == size) {
            addAtTail(val);
            return;
        }

        Node temp = head;

        for (int i = 0; i < index; i++) {
            temp = temp.next;
        }

        Node newNode = new Node(val);

        newNode.prev = temp.prev;
        newNode.next = temp;

        temp.prev.next = newNode;
        temp.prev = newNode;

        size++;
    }

    public void deleteAtIndex(int index) {
        if (index < 0 || index >= size)
            return;

        Node temp = head;

        for (int i = 0; i < index; i++) {
            temp = temp.next;
        }

        if (temp == head) {
            head = head.next;

            if (head != null)
                head.prev = null;
            else
                tail = null;

        } else if (temp == tail) {
            tail = tail.prev;
            tail.next = null;

        } else {
            temp.prev.next = temp.next;
            temp.next.prev = temp.prev;
        }

        size--;
    }
}