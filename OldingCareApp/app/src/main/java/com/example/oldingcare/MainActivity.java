package com.example.oldingcare;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import com.example.oldingcare.databinding.ActivityMainBinding;

public class MainActivity extends Activity {

    private TextView mTextView2,mTextView3;
    private ActivityMainBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        binding = ActivityMainBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        mTextView2 = binding.textView2;
        mTextView3 = binding.textView3;
    }

    public void Click1(View view) {
        Intent it= new Intent(this,MainActivity2.class);
        startActivity(it);
    }
}