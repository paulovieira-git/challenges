package com.example.oldingcare;

//import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.content.res.ColorStateList;
import android.os.Bundle;
import android.view.View;

public class MainActivity2 extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
    }

    public void chatButton(View view) {

    }

    public void activityButton(View view) {
        Intent intent=new Intent(this,MainActivity3.class);
        startActivity(intent);
    }

    public void medicalShedule(View view) {
        Intent intent=new Intent(this,MainActivity4.class);
        startActivity(intent);
    }

    public void inicio(View view) {
        Intent intent=new Intent(this,MainActivity.class);
        startActivity(intent);
    }
}